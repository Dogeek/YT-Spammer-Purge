from dataclasses import dataclass


@dataclass
class ScanInstance:
    matchedCommentsDict: dict
    vidIdDict: dict
    vidTitleDict: dict
    matchSamplesDict: dict
    authorMatchCountDict: dict
    allScannedCommentsDict: dict
    scannedRepliesCount: int
    scannedCommentsCount: int
    logTime: str
    logFileName: str
    errorOccurred: bool
