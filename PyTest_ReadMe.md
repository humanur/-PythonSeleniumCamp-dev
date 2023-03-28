    -Metotları başka bir metotları tetikleyerek kullanmayı sağlar 
    -Fonksiyonların üstlerinde kullanılır
    -Etiketleme (annotations) olarak da bilinir

    @pytest.fixture:  Testler arasında ortak bir durum veya kaynak paylaşmak için kullanılır. 
    Testlerinizin bir veritabanına bağlanmasını sağlar
    Örnek:
    @pytest.fixture
      def input_value():
        input = 39
        return input
    
    @pytest.mark.usefixtures: Belirli bir fixture'ı test fonksiyonunda kullanmak için kullanılır.
    Örnek:
    @pytest.mark.usefixtures('routes')
      def test_something():
        ...
    
    @pytest.mark.parametrize: Aynı test fonksiyonunu farklı parametrelerle birden fazla kez çalıştırmak için kullanılır. Testlerinizi daha 
    kapsamlı hale getirmenize ve farklı durumlarda farklı sonuçlar alıp almadığınızı kontrol etmenize olanak tanır.
    Örnek:
    @pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
      def test_multiplication_11(num, output):
        assert 11*num == output

    @pytest.mark.skip: Önüne yazıldığı fonksiyonun atlanmasını sağlar. 
    Örnek:
    @pytest.mark.skip()
      def test_the_unknown():
        ...

    @pytest.mark.skipif: Koşula bağlı olarak bir testi atlamamızı sağlar
    Örnek:
    @pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
      def test_function():
        ...
    
    @pytest.mark.slow:
    Örnek:
    @pytest.mark.slow
      def test_func_slow():
        pass
    
    @pytest.mark.timeout: Testin belirli bir süre içinde tamamlanmaya zorlar. Sonsuza kadar çalışmasını engeller.
    Örnek:
    @pytest.mark.timeout(60)
    def test_basic():
      with NsqdIntegrationServer() as server:
        conn = gnsq.Nsqd(server.address, http_port=server.http_port)
        assert conn.ping() == b'OK'
        assert 'topics' in conn.stats()
        assert 'version' in conn.info()
    
    @pytest.mark.xfail: Testin başarısız olmasını beklediğimiz furumlarda kullanılır.
    Örnek:
    @pytest.mark.xfail
      def test_function():
        ...
      
    @pytest.mark.filterwarnings:Testin belirli bir uyarı mesajını içermesi durumunda testin başarısız olması 
    gerektiğini belirtmek için kullanılır.
    Örnek:
    @pytest.mark.filterwarnings("ignore:api v1")
    def test_one():
      assert api_v1() == 1

    
    
    
    

    
