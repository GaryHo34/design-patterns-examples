# Facade Pattern

Today we talk about a really simple pattern, Facade pattern. It is a structural pattern, which means it is used to form large structures from simple ones. It is also a wrapper pattern, which means it wraps a complex subsystem with a simpler interface. 

The facade pattern is used to provide a unified interface to a set of interfaces in a subsystem. It defines a higher-level interface that makes the subsystem easier to use.
It is very intuitive to understand the facade pattern. Let's look at an example. Suppose we have a file convert factory, which can convert a TXT file to a PDF file. The convert process is complex, it needs to compress the TXT file first, then convert it to a PDF file. The code is as follows:

```java

class TXTFile {}
class CompressCodec {}
class CodecFactory {}
class PDFFile {}

public class FileConvertFactory {
    public PDFFile convert(TXTFile txtFile) {
        CompressCodec compressCodec = CodecFactory.getCompressCodec();
        // do something
        return new PDFFile();
    }
}

public class Client {
    public static void main(String[] args) {
        FileConvertFactory fileConvertFactory = new FileConvertFactory();
        TXTFile txtFile = new TXTFile();
        PDFFile pdfFile = fileConvertFactory.convert(txtFile);
    }
}
```

