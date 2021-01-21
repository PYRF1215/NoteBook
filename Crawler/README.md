# 爬蟲開發筆記

<ul>
  
  <li>
  <p><strong>爬蟲主題</strong></p>
  <ul>
  <li><a href="..." rel="nofollow"></a>主題1</li>       
  </ul>
  </li>
  
  
  <li>
  <p><strong>參考資料</strong></p>
  <ul>
  <li><a href="https://developer.mozilla.org/zh-TW/docs/Learn/Getting_started_with_the_web/HTML_basics" rel="nofollow">HTML 基礎</a></li>       
  <li><a href="">HTML 常用語法</a></li>
  </ul>
  </li>




  
  <li>
  <p><strong>擷取方式</strong></p>
  <ul>
  
  <li>本地端 
  <pre>
  <code>
    html_doc = """
        (a href="") test (/a)
    """
    from bs4 import BeautifulSoup
    sp = BeautifulSoup(html_doc,"html.parser")

    # html5lib = html.parser
  </code>
  </pre></li> 

  <li>複制上傳至GitHub擷取</li>

  <li>網站擷取
  <pre>
  <code>
    from bs4 import BeautifulSoup
    import requests
    html = requests.get('url').text
    sp = BeautifulSoup(html, 'html.parser')
  </code>
  </pre></li> 



</ul>    

  <li>
  <p><strong>相關程式碼</strong></p>
  <ul>

  <li>class替換方式
  <pre>
  <code>
    sp.find_all
    ('h4', 'card-title') = 
    ('h4', class_='card-title') = 
    ('h4', {'class': 'card-title'})
  </code>
  </pre></li> 

  <li>擷取超連結文字及網址
  <pre>
  <code>
    fd = sp.find_all('a')  
    for i in fd:  
    print(i.string)   #輸出超連結文字 
    print(i.get('href'))  #輸出超連結網址 
  </code>
  </pre></li> 






<h6>#常用套件</h6>
<table>
<thead>
<tr>
<th>項目</th>
<th align="center">說明</th>
</tr>  

<tr>
  <td>import bs4 from BeautifulSoup</td>
  <td>載入BeautifulSoup套件</td>
</tr> 

<tr>
  <td>import urllib3</td>
  <td>載入urllibs套件套件</td>
</tr> 


</tbody>
</table>
</thead>
<tbody>


<h6>#常用指令</h6>
<table>
<tbody>
<tr>
<th>指令</th>
<th>說明</th>
</tr>
<tr>
  <td>.text</td>
  <td>傳回去除所有HTML標籤，把網頁變為字串傳回</td>
</tr>  

<tr>
  <td>.prettify()</td>
  <td>HTML自動縮排</td>
</tr>



<tr>
  <td>strip()</td>
  <td>去字串頭尾空格</td>
</tr>

<tr>
  <td>\n</td>
  <td>換行</td>
</tr>

<tr>
  <td>print(sp.title)</td>
  <td>列印標題</td>
</tr>

<tr>
  <td>.status_code</td>
  <td>查詢狀態碼   200成功   404 失敗(找不到)</td>
</tr> 


<tr>
  <td>print(sp.title.string)</td>
  <td></td>
</tr> 

</tbody>
</table>


<h6>#常用語法</h6>
<table>
<tbody>

<tr>
<th>語法</th>
<th>說明</th>
</tr>

<tr>
  <td>print([s for s in x.stripped_strings])</td>
  <td>自動去掉空白字符串</td>
</tr>


</tbody>
</table>