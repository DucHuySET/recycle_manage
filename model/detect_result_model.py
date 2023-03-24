class DetectResult:
    def __init__(self, plateData, croppedImage, fullImage):
        self.plateData = plateData
        self.croppedImage = croppedImage
        self.fullImage = fullImage