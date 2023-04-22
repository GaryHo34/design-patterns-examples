

class TXTFile:
    pass
class CompressCodec:
    pass

class CodecFactory:
    def convert(self, cc:CompressCodec):
        return PDFFile();

class PDFFile :
    pass
class FileConvertFactory :
    def convert(self, txtFile: TXTFile) ->PDFFile:
        compressCodec =  CompressCodec();
        cf =  CodecFactory();
        # do something
        return cf.convert(compressCodec);

# Client
if __name__ == "__main__":
    ff = FileConvertFactory()
    ff.convert(TXTFile())
