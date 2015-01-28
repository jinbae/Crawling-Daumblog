
# Crawling-Daumblog

## Requirements

- Python 2.7
- Install [scrapy](http://scrapy.org)

        $pip install scrapy

## Items

- The item is defined in the class:

        daumblog.items.DaumblogItem

- See the source code for more details

## Spider : daum

- The `daum` spider scrapes the daumblog post (blog.daum.net)
- This spider crawls the entire blog.daum.net site (defined in the `start_urls` attribute)
- The basic form of a website : 

        "http://blog.daum.net/_blog/_top/sub/blogByCategorySubNew.do?category=101&list_type=recent&page_no=1"

## Pipelines

- This project uses a pipeline to extract all blog posts in a specific date(ex '2015-01-15')
- This pipeline is defined in the class:

        daumblog.pipelines.DaumblogPipeline

- So, before run the spider, check the pipeline source code

## Run
### Data crawling

        $ cd daumblog
        $ scrapy crawl daum -o daumblog.csv -t csv
        $ scrapy crawl daum -o daumblog.json -t json

- Be careful of running the code twice because the json file gets appended, rather than overwritten.

## Author

- [jinbae Im](http://github.com/jinbae)
