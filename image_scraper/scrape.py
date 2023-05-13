from bing_image_downloader import downloader

queries = ['Snake plant', 'Pothos', 'ZZ plant',  'Peace lily', 'Spider plant', 'Dracaena', 'Chinese evergreen',
           'Fiddle leaf fig', 'Rubber plant', 'Philodendron', 'Monstera', 'Dieffenbachia', 'Bird\'s nest fern',
           'Aloe vera', 'Boston fern', 'English ivy', 'Jade plant', 'Devil\'s ivy', 'Maidenhair fern',
           'String of pearls']


for q in queries:
    downloader.download(
        q,
        limit=10,
        output_dir='../data/plant_class',
        adult_filter_off=True,
        force_replace=False,
        timeout=60
    )
