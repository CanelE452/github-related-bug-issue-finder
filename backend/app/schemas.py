from typing import Literal

from pydantic import BaseModel, Field, field_validator

from .domain import repository_name


class AnalyzeRequest(BaseModel):
    repository_url: str = Field(max_length=300)
    extra_bug_labels: list[str] = Field(default_factory=list, max_length=30)
    refresh: bool = False
    prepare_semantic: bool = True

    @field_validator('repository_url')
    @classmethod
    def validate_repository(cls, value):
        return repository_name(value)

    @field_validator('extra_bug_labels')
    @classmethod
    def validate_labels(cls, value):
        if any(len(x) > 100 for x in value):
            raise ValueError('레이블은 100자 이하로 입력하세요.')
        return value


class SearchRequest(BaseModel):
    repository: str = Field(max_length=300)
    problem: str = Field(min_length=1, max_length=20000)
    error: str = Field(default='', max_length=40000)
    environment: str = Field(default='', max_length=5000)
    method: Literal['bm25', 'semantic', 'hybrid'] = 'hybrid'
    top_k: int = Field(default=5, ge=1, le=20)

    @field_validator('repository')
    @classmethod
    def validate_repository(cls, value):
        return repository_name(value)

    @field_validator('problem')
    @classmethod
    def not_blank(cls, value):
        if not value.strip():
            raise ValueError('문제 설명을 입력하세요.')
        return value.strip()
