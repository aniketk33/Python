from google.cloud import translate, storage
from os import environ
print(environ.get("GOOGLE_APPLICATION_CREDENTIALS","HEYYY"))
storage_client = storage.Client()

# Make an authenticated API request
buckets = list(storage_client.list_buckets())
print(buckets)

# project_id = "datatoexcel-322112"
# assert project_id

# transclient = translate.TranslationServiceClient()
# parent = f"projects/{project_id}"
# # client = translate.TranslationServiceClient()
# # #cleartranslate.
# response = transclient.get_supported_languages(parent=parent, display_language_code="en")
# languages = response.languages

# print(f" Languages: {len(languages)} ".center(60, "-"))
# for language in languages:
#     print(f"{language.language_code}\t{language.display_name}")

# client = translate.Translation("AIzaSyAq6P_G2iQHgIwFwN3rKsIwTpNl5fIw3ck")
# response = client.get_supported_languages(display_language_code="en")
# languages = response.languages

# print(f" Languages: {len(languages)} ".center(60, "-"))
# for language in languages:
#     print(f"{language.language_code}\t{language.display_name}")
