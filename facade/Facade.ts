class TXTFile {
}

class CompressCodec {
}

class PDFFile {
}

class CodecFactory {
    convert(cc: CompressCodec): PDFFile {
        return new PDFFile();
    }
}


class FileConvertFactory {
    public convert(txtFile: TXTFile): PDFFile {
        const compressCodec: CompressCodec = new CompressCodec();
        const cf: CodecFactory = new CodecFactory();
        // do something
        return cf.convert(compressCodec);
    }
}

const ff = new FileConvertFactory();
ff.convert(new TXTFile())