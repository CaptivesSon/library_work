from smart_open import open


def stream_uri(uri_in, uri_out, chunk_size=1 << 18):  # 256kB chunks
    """Write from uri_in to uri_out with minimal memory footprint."""
    with open(uri_in, "rb") as fin, open(uri_out, "wb") as fout:
        while chunk := fin.read(chunk_size):
            fout.write(chunk)


# from https to disk
stream_uri("https://www.dizigom.tv/sherlock-3-sezon-1-bolum-hd1/", ".sherlock-3-sezon-1-bolum-hd1/")
# from s3 to ftp
stream_uri("s3://bucket1/example.pdf", "ftp://192.168.178.1:21/example.pdf")