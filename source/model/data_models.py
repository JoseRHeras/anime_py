from dataclasses import dataclass
from typing import Dict

@dataclass
class Show:
    title_id: str
    links: str
    synopsis: str
    titles: Dict
    canonical_title: str
    image: str


def parse_to_show_object(data: Dict):
    try:
        title_id = data["id"]
        links = data["links"]["self"]
        synopsis = data["attributes"]["synopsis"]
        titles = data["attributes"]["titles"]
        canonical_title = data["attributes"]["canonicalTitle"]
        image = data["attributes"]["posterImage"]["original"]

        return Show(
            title_id=title_id, 
            links=links, 
            synopsis=synopsis, 
            titles=titles, 
            canonical_title=canonical_title,
            image=image
        )

    except Exception:
        return None

#  {
        #     "id": "13003",
        #     "type": "anime",
        #     "links": {
        #         "self": "https://kitsu.io/api/edge/anime/13003"
        #     },
        #     "attributes": {
        #         "createdAt": "2017-01-22T00:10:06.336Z",
        #         "updatedAt": "2022-01-05T00:00:09.298Z",
        #         "slug": "zhu-shen-de-zicai-baofan",
        #         "synopsis": "Chinese mythical gods timed traveled to 21st century.",
        #         "description": "Chinese mythical gods timed traveled to 21st century.",
        #         "coverImageTopOffset": 0,
        #         "titles": {
        #             "en_jp": "Zhu shen de zicai baofan",
        #             "ja_jp": "诸神的紫菜包饭"
        #         },
        #         "canonicalTitle": "Zhu shen de zicai baofan",
        #         "abbreviatedTitles": [],
        #         "averageRating": null,
        #         "ratingFrequencies": {
        #             "2": "0",
        #             "3": "0",
        #             "4": "0",
        #             "5": "0",
        #             "6": "0",
        #             "7": "0",
        #             "8": "0",
        #             "9": "0",
        #             "10": "0",
        #             "11": "0",
        #             "12": "0",
        #             "13": "0",
        #             "14": "1",
        #             "15": "0",
        #             "16": "0",
        #             "17": "0",
        #             "18": "0",
        #             "19": "0",
        #             "20": "0"
        #         },
        #         "userCount": 93,
        #         "favoritesCount": 1,
        #         "startDate": "2016-06-17",
        #         "endDate": null,
        #         "nextRelease": null,
        #         "popularityRank": 11065,
        #         "ratingRank": null,
        #         "ageRating": "PG",
        #         "ageRatingGuide": "Children",
        #         "subtype": "ONA",
        #         "status": "current",
        #         "tba": null,
        #         "posterImage": {
        #             "tiny": "https://media.kitsu.io/anime/poster_images/13003/tiny.jpg",
        #             "large": "https://media.kitsu.io/anime/poster_images/13003/large.jpg",
        #             "small": "https://media.kitsu.io/anime/poster_images/13003/small.jpg",
        #             "medium": "https://media.kitsu.io/anime/poster_images/13003/medium.jpg",
        #             "original": "https://media.kitsu.io/anime/poster_images/13003/original.jpg",
        #             "meta": {
        #                 "dimensions": {
        #                     "tiny": {
        #                         "width": null,
        #                         "height": null
        #                     },
        #                     "large": {
        #                         "width": null,
        #                         "height": null
        #                     },
        #                     "small": {
        #                         "width": null,
        #                         "height": null
        #                     },
        #                     "medium": {
        #                         "width": null,
        #                         "height": null
        #                     }
        #                 }
        #             }
        #         },
        #         "coverImage": null,
        #         "episodeCount": null,
        #         "episodeLength": 10,
        #         "totalLength": 30,
        #         "youtubeVideoId": null,
        #         "showType": "ONA",
        #         "nsfw": false
        #     },
        # },