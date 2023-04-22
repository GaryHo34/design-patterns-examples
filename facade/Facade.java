public class Facade {
    class TXTFile {
    }

    class CompressCodec {
    }

    class CodecFactory {

        public PDFFile convert(CompressCodec cc) {
            return new PDFFile();
        }
    }

    class PDFFile {
    }

    public class FileConvertFactory {
        public PDFFile convert(TXTFile txtFile) {
            CompressCodec compressCodec = new CompressCodec();
            CodecFactory cf = new CodecFactory();
            // do something
            return cf.convert(compressCodec);
        }
    }

    public void testFileConvertFactory() {
        FileConvertFactory ff = new FileConvertFactory();
        ff.convert(new TXTFile());
    }

    public static void main(String[] args) {
        Facade fc = new Facade();
        fc.testFileConvertFactory();
    }
}