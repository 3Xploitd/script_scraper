def script_scraper(url):
    r = requests.get(url)
    script_regex = re.findall(r'<script.*?>[\w\s\W\d\.]+?</script>',r.text)
        for each in script_regex:
            if each != []:
                print(each,"\n")
            else:
                continue
