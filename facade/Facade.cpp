#include <iostream>
#include <string>

using namespace std;

class TXTFile
{
};

class CompressCodec
{
};

class PDFFile
{
};

class CodecFactory
{
public:
    PDFFile *convert(CompressCodec *cc)
    {
        return new PDFFile();
    }
};

class FileConvertFactory
{
public:
    PDFFile *convert(TXTFile *txtFile)
    {
        CompressCodec *compressCodec = new CompressCodec();
        CodecFactory *cf = new CodecFactory();
        // do something
        return cf->convert(compressCodec);
    }
};

// as a client
int main(int argc, char *argv[])
{
    FileConvertFactory *ff = new FileConvertFactory();
    ff->convert(new TXTFile());
}