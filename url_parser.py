'''
Script parses url like <host>,<domain>,<path>,[parameters]
'''
import re

protocols = ['https', 'http', 'ftp']

def parse_url(url):
  if isinstance(url, str):
    url = url.lower()
    for protocol in protocols:
      result = '^({0}:\/\/)([\S\w][^?\/]*)([\/|\?]?)([\S]*)'.format(protocol)
      if(re.search(result, url)):
        result_array = re.search(result, url).groups()
        print('URL: ' + url + '\n' + '**********')
        summary = ''
        summary += 'Protocol: ' + result_array[0] + '\n' + 'Host: ' + result_array[1] + '\n'
        if(result_array[2] == '/'):
          summary += 'Path: ' + result_array[3] + '\n'
        elif(result_array[2] == '?'):
          summary += 'Parameters: ' + result_array[3] + '\n'
        return summary
    return 'Undefined protocol'
  else:
    print('It\'s not URL. Enter URL')


print(parse_url('http://ya.ru?user=superuser&password=pass123'))
print(parse_url('https://ya.ru/registration'))