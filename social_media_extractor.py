import re

class SocialMediaExtractor():
    """
        This class should extract social medias cited in some text as well as generic hiperlinks
        to be used eventually in natural language processing projects.
    """
    __social_media = set(['facebook', 'instagram', 'twitter', 'youtube'])

    @staticmethod
    def extract_instagram(text: str):
        return list(set(re.findall(r"(instagram.com/[a-zA-Z0-9_\-\./]*)", text)))

    @staticmethod
    def extract_facebook(text: str) -> list:
        return list(set(re.findall(r"(facebook.com/[a-zA-Z0-9_\-\./]*)", text)))

    @staticmethod
    def extract_twitter(text: str):
        return list(set(re.findall(r"(twitter.com/[a-zA-Z0-9_\-\./]*)", text)))

    @staticmethod
    def extract_website(text: str, exclude_social_media: bool=True, remove_protocol: bool=True):
        websites = [m.group('website') for m in re.finditer(r"(?P<website>(https?://|www)[\.a-zA-Z0-9_/\-]+)", text)]
        
        if not exclude_social_media:
            return websites

        filtered_websites = []
        for word in websites:
            for social_media in SocialMediaExtractor.__social_media:
                if social_media in word:
                    break
            else:
                filtered_websites.append(word)
        filtered_websites = SocialMediaExtractor.__remove_protocols(set(filtered_websites))
        return list(set(filtered_websites))

    @staticmethod
    def extract_youtube(text: str):
        return list(set(re.findall(r"((youtube.com|youtube.com.br)/[a-zA-Z0-9_]*)", text)))

    @staticmethod
    def __remove_protocols(site_list: list) -> list:
        return [s.replace('https://', '').replace('http://', '').replace('www.', '') for s in set(site_list)]

