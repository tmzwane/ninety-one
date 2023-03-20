import os

ABS_PATH = os.path.dirname(os.path.abspath(__file__))
defaultTestFile = os.path.join(ABS_PATH, "..", "datasets", "TestData.csv")

class CustomParser:
    def __init__(self, fileLocation: str = defaultTestFile, delimiter: str = ",") -> None:
        if os.path.isfile(fileLocation):
            self.fileLocation = fileLocation
        else:
            self.fileLocation = defaultTestFile

        self.delimiter = delimiter
        self.rawContents = None
        self.parsedContents = None
        self.processedData = []

    def set_file_location(self, fileLocation: str) -> bool:
        if os.path.isfile(fileLocation):
            self.fileLocation = fileLocation
            return True
        return False
    
    def process_file_contents(self) -> bool:
        if self.fileLocation:
            try:
                with open(self.fileLocation) as file:
                    self.rawContents = file.read()
                if self.rawContents:
                    return True
                return False
            except Exception:
                return False
        return False
    
    def parse_raw_contents(self) -> bool:
        if self.rawContents:
            try:
                self.parsedContents = self.rawContents.split("\n")
                return True
            except Exception:
                return False
        return False

    def parse_delimited_contents(self) -> list:
        headingProcessed = False
        blueprintStructSet = False
        blueprintStruct = {}

        processedHeadings = []
        expectedColumns = 0

        for content in self.parsedContents:
            if not headingProcessed:
                headings = content.split(",")
                expectedColumns = len(headings)
            
                if expectedColumns > 0:
                    headingProcessed = True
            
            if headingProcessed and not blueprintStructSet:
                for heading in headings:
                    heading = heading.strip()
                    if heading:
                        processedHeadings.append(heading)
                        blueprintStruct[heading] = None

                cleanedHeadings = list(blueprintStruct.keys())
                if len(cleanedHeadings) > 0:
                    expectedColumns = len(cleanedHeadings)
                    blueprintStructSet = True
                    continue
            
            if blueprintStructSet:
                data = blueprintStruct.copy()
                row = content.split(",")

                if len(row) == expectedColumns:
                    for idx, dictKey in enumerate(processedHeadings):
                        data[dictKey] = row[idx]
                
                    self.processedData.append(data)

        return self.processedData
    
    def reset_processed_data(self):
        self.processedData = []
