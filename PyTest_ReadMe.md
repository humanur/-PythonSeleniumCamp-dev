    -Metotları başka bir metotları tetikleyerek kullanmayı sağlar
    -Fonksiyonların üstlerinde kullanılır
    -Etiketleme (annotations) olarak da bilinir
    
    @pytest.fixture,
    
    @pytest.fixture
    def cmdopt(request):
        return request.config.getoption("--cmdopt")
    @pytest.mark.parametrize
    @pytest.mark.skip
    @pytest.mark.skipif
    @pytest.mark.usefixtures
    @pytest.mark.xfail
    @pytest.mark.filterwarnings
    
    @pytest.approx
    @pytest.fixture
    @pytest.param
    @pytest.yield_fixture
    @pytest.exit
    @pytest.fail
    @pytest.freeze_includes
    
    @pytest.mark._config
    @pytest.mark._markers
    @pytest.mark.__annotations__
    @pytest.mark.__dict__
    @pytest.mark.__doc__
    @pytest.mark.__module__
