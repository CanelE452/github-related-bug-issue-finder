import React, { useEffect, useRef, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { ArrowUpRight, ArrowRight, Search, Github, CircleDot, CircleCheck, Layers, SlidersHorizontal, LoaderCircle, AlertCircle, X, Terminal, GitBranch, Check, Command } from 'lucide-react';
import './style.css';

type Method = 'bm25' | 'semantic' | 'hybrid';
type Job = { id: string; repository: string; status: string; fetched_count?: number; issue_count?: number; bug_issue_count?: number; embedded_count?: number; partial?: boolean; collected_at?: string; cache_hit?: boolean; available_methods: Method[]; error?: {message: string}; semantic_error?: {message: string} };
type Result = {number: number; title: string; labels: string[]; state: string; excerpt: string; score: number; url: string};
type SearchResult = {repository: string; method: Method; results: Result[]; elapsed_ms: number; partial: boolean; collected_at: string; score_type: string};
const methodNames = {bm25: '키워드', semantic: '의미 기반', hybrid: 'Hybrid'};
const stages: Record<string, string> = {queued: '분석 대기 중', fetching: 'GitHub Issue 수집 중', indexing_bm25: '키워드 인덱스 생성 중', indexing_semantic: '다국어 인덱스 생성 중', completed: '분석 완료', failed: '분석 실패'};
async function api<T>(path: string, body?: unknown, signal?: AbortSignal): Promise<T> {
  const r = await fetch('/api' + path, {method: body === undefined ? 'GET' : 'POST', headers: {'Content-Type': 'application/json'}, body: body === undefined ? undefined : JSON.stringify(body), signal});
  const d = await r.json();
  if (!r.ok) throw new Error(d.error?.message || (Array.isArray(d.detail) ? d.detail.map((x: {msg: string}) => x.msg).join(' · ') : '요청에 실패했습니다. 서버 연결을 확인하세요.'));
  return d;
}

function App() {
  const [repo, setRepo] = useState('https://github.com/huggingface/transformers');
  const [labels, setLabels] = useState('');
  const [semantic, setSemantic] = useState(true);
  const [refresh, setRefresh] = useState(false);
  const [advanced, setAdvanced] = useState(false);
  const [jobId, setJobId] = useState('');
  const [job, setJob] = useState<Job | null>(null);
  const [analyzing, setAnalyzing] = useState(false);
  const [problem, setProblem] = useState('');
  const [errorInput, setErrorInput] = useState('');
  const [environment, setEnvironment] = useState('');
  const [method, setMethod] = useState<Method>('hybrid');
  const [error, setError] = useState('');
  const [searching, setSearching] = useState(false);
  const [result, setResult] = useState<SearchResult | null>(null);
  const requestVersion = useRef(0);
  const searchAbort = useRef<AbortController | null>(null);
  const ready = !!job?.available_methods.includes(method);

  useEffect(() => {
    if (!jobId) return;
    const controller = new AbortController();
    let timer: ReturnType<typeof setTimeout>;
    async function poll() {
      try {
        const next = await api<Job>('/repositories/jobs/' + jobId, undefined, controller.signal);
        setJob(next);
        if (['completed', 'failed'].includes(next.status)) {setAnalyzing(false); return;}
        timer = setTimeout(poll, 1400);
      } catch (e) {
        if (!controller.signal.aborted) {setError((e as Error).message); setAnalyzing(false);}
      }
    }
    void poll();
    return () => {controller.abort(); clearTimeout(timer);};
  }, [jobId]);
  useEffect(() => () => {searchAbort.current?.abort();}, []);

  async function analyze(e: React.FormEvent) {
    e.preventDefault(); setError(''); setAnalyzing(true); setJob(null); setResult(null); setJobId('');
    requestVersion.current++; searchAbort.current?.abort(); setSearching(false);
    try {
      const next = await api<{job_id: string}>('/repositories/analyze', {repository_url: repo, extra_bug_labels: labels.split(',').map(x => x.trim()).filter(Boolean), prepare_semantic: semantic, refresh});
      setJobId(next.job_id);
    } catch (e) {setError((e as Error).message); setAnalyzing(false);}
  }
  async function search(e: React.FormEvent) {
    e.preventDefault(); if (!job) return;
    setError(''); setSearching(true); setResult(null);
    const version = ++requestVersion.current;
    searchAbort.current?.abort();
    searchAbort.current = new AbortController();
    try {
      const next = await api<SearchResult>('/search', {repository: job.repository, problem, error: errorInput, environment, method, top_k: 5}, searchAbort.current.signal);
      if (version === requestVersion.current) setResult(next);
    } catch (e) {if (version === requestVersion.current && (e as Error).name !== 'AbortError') setError((e as Error).message);}
    finally {if (version === requestVersion.current) setSearching(false);}
  }
  function example() {setProblem('모델을 불러올 때 GPU 메모리가 부족해서 실행이 멈춰요.'); setErrorInput('RuntimeError: CUDA out of memory'); setEnvironment('Python 3.12 · CUDA');}

  return <>
    <header className="topbar"><a className="brand" href="/" aria-label="Issue Finder 홈"><span className="brand-icon"><Layers size={20}/></span>Issue Finder<span className="beta">LOCAL</span></a><a className="docs-link" href="/docs" target="_blank" rel="noreferrer">API 문서 <ArrowUpRight size={14}/></a></header>
    <main>
      <section className="intro"><div className="eyebrow"><span/> GITHUB BUG EXPLORER</div><h1>문제 설명으로<br/><span>관련 GitHub Bug Issue 찾기</span></h1><p>겪고 있는 문제를 설명해 주세요. 저장소의 기존 Bug Issue에서<br className="desktop-break"/> 관련된 논의를 한국어와 영어로 찾아드립니다.</p></section>
      <div className="workspace">
        <aside>
          <section className="panel repo-panel"><div className="panel-heading"><span className="step">01</span><h2>어디에서 발생했나요?</h2><Github size={18}/></div><p className="muted small">검색할 공개 GitHub 저장소를 연결하세요.</p>
            <form onSubmit={analyze}><label htmlFor="repository">저장소 URL</label><div className="input-icon"><Github size={16}/><input id="repository" value={repo} onChange={e => setRepo(e.target.value)} placeholder="https://github.com/owner/repo" required maxLength={300} disabled={analyzing}/></div>
              <button className="advanced-toggle" type="button" aria-expanded={advanced} onClick={() => setAdvanced(!advanced)}><SlidersHorizontal size={14}/> 분석 설정 <span>{advanced ? '−' : '+'}</span></button>
              {advanced && <div className="advanced"><label htmlFor="labels">추가 Bug 레이블 <span>쉼표로 구분</span></label><input id="labels" value={labels} onChange={e => setLabels(e.target.value)} placeholder="type: bug, regression" disabled={analyzing}/><label className="check"><input type="checkbox" checked={semantic} onChange={e => setSemantic(e.target.checked)} disabled={analyzing}/> 다국어 검색 준비</label><label className="check"><input type="checkbox" checked={refresh} onChange={e => setRefresh(e.target.checked)} disabled={analyzing}/> GitHub에서 새로 수집</label><p className="hint">기본 Bug 레이블과 Issue 유형을 함께 확인합니다.</p></div>}
              <button className="button secondary full" disabled={analyzing} type="submit">{analyzing ? <><LoaderCircle size={16} className="spin"/> 분석 중</> : <>저장소 분석 <ArrowRight size={16}/></>}</button>
            </form>
            {job && <div className={'job ' + (job.status === 'failed' ? 'failed' : '')} aria-live="polite"><div className="job-title">{analyzing ? <LoaderCircle size={15} className="spin"/> : job.status === 'failed' ? <AlertCircle size={15}/> : <CircleCheck size={15}/>} {stages[job.status]}</div><p className="repo-name"><GitBranch size={13}/>{job.repository}</p><div className="stats"><div><strong>{job.fetched_count?.toLocaleString() ?? '—'}</strong><span>조회 항목 · PR 포함</span></div><div><strong>{job.bug_issue_count?.toLocaleString() ?? '—'}</strong><span>Bug Issue</span></div></div>{job.embedded_count !== undefined && analyzing && <p className="hint">임베딩 {job.embedded_count} / {job.bug_issue_count}</p>}{job.partial && <p className="notice">최신 최대 20페이지를 수집한 결과입니다. 저장소 전체가 아닙니다.</p>}{job.collected_at && <p className="hint">{job.cache_hit ? '캐시 사용 · ' : ''}{new Date(job.collected_at).toLocaleString('ko-KR')}</p>}{job.error && <p className="notice">{job.error.message}</p>}{job.semantic_error && <p className="notice">{job.semantic_error.message} 키워드 검색은 사용할 수 있습니다.</p>}</div>}
          </section>
          <div className="side-note"><span className="mini-icon"><Command size={17}/></span><div><strong>단어가 달라도, 문제는 같을 수 있어요.</strong><p>키워드와 문장의 의미를 함께 살펴<br/>관련된 Issue를 찾습니다.</p></div></div>
        </aside>
        <div className="content-column">
          <section className="panel query-panel"><div className="panel-heading"><span className="step">02</span><h2>어떤 문제가 생겼나요?</h2><span className="language-badge">한국어 · English</span></div>
            <form onSubmit={search}><label htmlFor="problem">문제 설명 <span className="required">필수</span></label><textarea id="problem" className="problem" value={problem} onChange={e => setProblem(e.target.value)} placeholder="예: 모델을 업데이트한 뒤 CPU 환경에서 실행하면 프로그램이 종료돼요." required maxLength={20000}/>
              <div className="optional-fields"><div><label htmlFor="error-input"><Terminal size={14}/> 오류 메시지 <span>선택</span></label><textarea id="error-input" className="code" value={errorInput} onChange={e => setErrorInput(e.target.value)} placeholder={"RuntimeError: …\n오류 메시지나 stack trace를 붙여넣으세요."} maxLength={40000}/></div><div><label htmlFor="environment">실행 환경 <span>선택</span></label><textarea id="environment" value={environment} onChange={e => setEnvironment(e.target.value)} placeholder={"OS, 라이브러리 버전, 실행 장치 등\nUbuntu 24.04 / Python 3.12 / CPU"} maxLength={5000}/></div></div>
              <div className="search-actions"><div className="method-control"><label htmlFor="method">검색 방식</label><select id="method" value={method} onChange={e => setMethod(e.target.value as Method)}><option value="hybrid">Hybrid · 키워드 + 의미</option><option value="semantic">의미 기반 · 다국어</option><option value="bm25">키워드 · BM25</option></select></div><button className="button primary" disabled={!ready || searching || !problem.trim()} type="submit">{searching ? <LoaderCircle size={16} className="spin"/> : <Search size={16}/>} {searching ? '검색 중' : '관련 Issue 찾기'}</button></div>
              {!ready && <p className="hint readiness">{job?.available_methods.includes('bm25') ? '선택한 검색 방식이 아직 준비되지 않았습니다. 키워드 검색을 선택할 수 있어요.' : '저장소 분석을 완료하면 검색할 수 있어요.'}</p>}
            </form>
          </section>
          {error && <div className="error-banner" role="alert"><AlertCircle size={17}/><span>{error}</span><button onClick={() => setError('')} aria-label="오류 닫기"><X size={16}/></button></div>}
          <section className="results" aria-live="polite" aria-busy={searching}><div className="results-heading"><h2>관련 Issue {result && <span>{result.results.length}</span>}</h2><span>{result ? `${methodNames[result.method]} · ${(result.elapsed_ms / 1000).toFixed(2)}초` : 'TOP 5'}</span></div>
            {searching ? <div className="empty"><LoaderCircle size={28} className="spin"/><h3>관련된 논의를 찾고 있어요</h3><p>첫 검색은 모델을 불러오는 시간이 추가될 수 있어요.</p></div> : result ? result.results.length ? <><p className="result-context">{result.repository} · {result.partial ? '수집 범위 내 검색' : '수집된 Issue 검색'}</p>{result.results.map((x, i) => <article className="result-card" key={x.number}><div className="result-top"><span className="result-number">{String(i + 1).padStart(2, '0')}</span><span className={'state ' + x.state}>{x.state === 'open' ? <CircleDot size={13}/> : <CircleCheck size={13}/>} {x.state === 'open' ? 'Open' : 'Closed'}</span><span className="issue-number">#{x.number}</span><span className="score" title="검색 방식별 관련도이며 중복 확률이 아닙니다.">{result.score_type} {x.score.toFixed(result.method === 'hybrid' ? 4 : 3)}</span></div><a className="result-title" href={x.url} target="_blank" rel="noreferrer">{x.title}<ArrowUpRight size={18}/></a><p className="excerpt">{x.excerpt || '본문이 없는 Issue입니다.'}</p><div className="result-bottom"><div className="labels">{x.labels.slice(0, 6).map(label => <span key={label}>{label}</span>)}</div><a href={x.url} target="_blank" rel="noreferrer">GitHub에서 보기 <ArrowUpRight size={13}/></a></div></article>)}<p className="results-footnote"><Check size={13}/> 관련도는 중복 확률이 아닙니다. 원문에서 같은 문제인지 확인하세요.</p></> : <div className="empty"><Search size={28}/><h3>일치하는 키워드를 찾지 못했어요</h3><p>다른 오류 코드나 함수명을 입력하거나 의미 기반 검색을 사용해 보세요.</p></div> : <div className="empty"><div className="empty-illustration"><div/><div/><div/><span><Search size={24}/></span></div><h3>문제의 실마리는 여기에서</h3><p>저장소를 연결하고 문제를 설명하면<br/>관련된 기존 Issue가 이곳에 나타납니다.</p><button className="example-button" onClick={example}>예시 입력해 보기 <ArrowRight size={13}/></button></div>}
          </section>
        </div>
      </div>
      <footer><span><Layers size={13}/> Issue Finder</span><span>공개 저장소 · Bug Issue · 근거가 있는 탐색</span></footer>
    </main>
  </>;
}

createRoot(document.getElementById('root')!).render(<React.StrictMode><App/></React.StrictMode>);
