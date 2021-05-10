import requests

CRX_URL_PREFIX = r"https://clients2.google.com/service/update2/crx?response=redirect&prodversion=45&acceptformat" \
                 r"=crx2,crx3&x=id%3D"
CRX_URL_SUFFIX = r"%26uc"


ext_id = 'kdfieneakcjfaiglcfcgkidlkmlijjnh'
make_crx_url = lambda extid: CRX_URL_PREFIX + extid + CRX_URL_SUFFIX
crx_url = make_crx_url(ext_id)
file_name = ext_id+'.crx'
print("crx_url:: ",crx_url)
response = requests.get(crx_url, allow_redirects=True)
with open(file_name, 'wb') as f:
    f.write(response.content)
