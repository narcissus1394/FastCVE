# generated by datamodel-codegen:
#   filename:  cve.json
#   timestamp: 2023-03-02T09:59:46+00:00

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Extra, Field, confloat, constr
from .cvss_v2 import CveCvssDataModel as CveCvssDataV2
from .cvss_v30 import CveCvssDataModel as CveCvssDataV30
from .cvss_v31 import CveCvssDataModel as CveCvssDataV31


class Type(Enum):
    Primary = 'Primary'
    Secondary = 'Secondary'


class LangString(BaseModel):
    class Config:
        extra = Extra.forbid

    lang: str
    value: constr(max_length=4096)


class Reference(BaseModel):
    class Config:
        extra = Extra.forbid

    url: constr(regex=r'^(ftp|http)s?://\S+$', max_length=500)
    source: Optional[str] = None
    tags: Optional[List[str]] = None


class VendorComment(BaseModel):
    class Config:
        extra = Extra.forbid

    organization: str
    comment: str
    lastModified: datetime


class Weakness(BaseModel):
    class Config:
        extra = Extra.forbid

    source: str
    type: str
    description: List[LangString] = Field(..., min_items=0)


class Operator(Enum):
    AND = 'AND'
    OR = 'OR'


class CpeMatch(BaseModel):
    """
    CPE match string or range
    """

    class Config:
        extra = Extra.forbid

    vulnerable: bool
    criteria: str
    matchCriteriaId: UUID
    versionStartExcluding: Optional[str] = None
    versionStartIncluding: Optional[str] = None
    versionEndExcluding: Optional[str] = None
    versionEndIncluding: Optional[str] = None


class CvssV2(BaseModel):
    class Config:
        extra = Extra.forbid

    source: str
    type: Type
    cvssData: CveCvssDataV2
    baseSeverity: Optional[str] = None
    exploitabilityScore: Optional[confloat(ge=0.0, le=10.0)] = Field(
        None, description='CVSS subscore.'
    )
    impactScore: Optional[confloat(ge=0.0, le=10.0)] = Field(
        None, description='CVSS subscore.'
    )
    acInsufInfo: Optional[bool] = None
    obtainAllPrivilege: Optional[bool] = None
    obtainUserPrivilege: Optional[bool] = None
    obtainOtherPrivilege: Optional[bool] = None
    userInteractionRequired: Optional[bool] = None


class CvssV30(BaseModel):
    class Config:
        extra = Extra.forbid

    source: str
    type: Type
    cvssData: CveCvssDataV30 
    exploitabilityScore: Optional[confloat(ge=0.0, le=10.0)] = Field(
        None, description='CVSS subscore.'
    )
    impactScore: Optional[confloat(ge=0.0, le=10.0)] = Field(
        None, description='CVSS subscore.'
    )


class CvssV31(BaseModel):
    class Config:
        extra = Extra.forbid

    source: str
    type: Type
    cvssData: CveCvssDataV31
    exploitabilityScore: Optional[confloat(ge=0.0, le=10.0)] = Field(
        None, description='CVSS subscore.'
    )
    impactScore: Optional[confloat(ge=0.0, le=10.0)] = Field(
        None, description='CVSS subscore.'
    )

class Epss(BaseModel):
    class Config:
        extra = Extra.forbid

    score: float
    percentile: float
    Date: datetime

class Node(BaseModel):
    """
    Defines a configuration node in an NVD applicability statement.
    """

    class Config:
        extra = Extra.forbid

    operator: Operator
    negate: Optional[bool] = None
    cpeMatch: List[CpeMatch]


class Metrics(BaseModel):
    """
    Metric scores for a vulnerability as found on NVD.
    """

    class Config:
        extra = Extra.forbid

    cvssMetricV31: Optional[List[CvssV31]] = Field(None, description='CVSS V3.1 score.')
    cvssMetricV30: Optional[List[CvssV30]] = Field(None, description='CVSS V3.0 score.')
    cvssMetricV2: Optional[List[CvssV2]] = Field(None, description='CVSS V2.0 score.')
    epssScoreGt: Optional[List[Epss]] = Field(None, descexitription='EPSS score greater than.')
    epssScoreLt: Optional[List[Epss]] = Field(None, description='EPSS score less than.')
    epssPercGt: Optional[List[Epss]] = Field(None, description='EPSS percentile greater than.')
    epssPercLt: Optional[List[Epss]] = Field(None, description='EPSS percentile less than.')

class Config(BaseModel):
    class Config:
        extra = Extra.forbid

    operator: Optional[Operator] = None
    negate: Optional[bool] = None
    nodes: List[Node]

class CveItem(BaseModel):
    class Config:
        extra = Extra.forbid

    id: constr(regex=r'^CVE-[0-9]{4}-[0-9]{4,}$')
    sourceIdentifier: Optional[str] = None
    vulnStatus: Optional[str] = None
    published: datetime
    lastModified: datetime
    evaluatorComment: Optional[str] = None
    evaluatorSolution: Optional[str] = None
    evaluatorImpact: Optional[str] = None
    cisaExploitAdd: Optional[date] = None
    cisaActionDue: Optional[date] = None
    cisaRequiredAction: Optional[str] = None
    cisaVulnerabilityName: Optional[str] = None
    descriptions: List[LangString] = Field(..., min_items=1)
    references: List[Reference] = Field(..., max_items=500, min_items=0)
    metrics: Optional[Metrics] = Field(
        None, description='Metric scores for a vulnerability as found on NVD.'
    )
    weaknesses: Optional[List[Weakness]] = None
    configurations: Optional[List[Config]] = None
    vendorComments: Optional[List[VendorComment]] = None


class DefCveItem(BaseModel):
    class Config:
        extra = Extra.forbid

    cve: CveItem


class CveModel(BaseModel):
    class Config:
        extra = Extra.forbid

    resultsPerPage: int
    startIndex: int
    totalResults: int
    format: str
    version: str
    timestamp: datetime
    vulnerabilities: List[DefCveItem] = Field(..., description='NVD feed array of CVE')
