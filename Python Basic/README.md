# 資料結構

<h6>格式化函數</h6> 
<table>
<thead>
<tr>
<th>數字</th>
<th>格式</th>
<th>輸出</th>
<th>描述</th>
</tr>
</thead>


<tbody>

<tr>
<td>3.1415926</td>
<td>{:.2f}</td>
<td>3.14</td>
<td>保留小數點後兩位</td>
<tr>

<tr>
<td>1215</td>
<td>{:<10d}</td>
<td>1215</td>
<td>
<:左對齊 (寬度為10)<br>
^:中
</td>
</tr>



<tr align="center">
<td colspan="4">Remarks</td></td>
</tr>

<tr>
<td>%s</td> 
<td>字符串 (採用str()的顯示)</td>
<td>%r</td>
<td>字符串 (採用repr()的顯示)</td>
</tr>

<tr>
<td>%c</td>
<td>單個字符</td>
<td>%b</td>
<td>二進制整數</td>
</tr>
 
<tr>
<td>%d</td>
<td>十進制整數</td>
<td>%i</td>
<td>十進制整數</td>
</tr>

<tr>
<td>%o</td>
<td>八進制整數</td>
<td>%x</td>
<td>十六進制整數</td>
</tr>
 
<tr>
<td>%e</td>
<td>指數 (基底寫為e)</td>
<td>%E</td>
<td>指數 (基底寫為E)</td>
</tr> 


<tr>
<td>%f</td>
<td>浮點數</td>
<td>%F</td>
<td>浮點數，與上相同%g 指數(e)或浮點數 (根據顯示長度)</td>
</tr> 
 
<tr>
<td>%G</td>
<td>指數(E)或浮點數 (根據顯示長度)</td>
<td>%%</td>
<td>字符"%"</td>
</tr>
 
</tbody>

</table>





<h6>#基本運算式</h6>
<table>
<thead>
<th>運算符號</th>
<th>功能</th>
</thead>

<tbody>
<tr>
<td>%</td>
<td>取餘數</td>
</tr>

<tr>
<td>**</td>
<td>次方</td>
</tr>

</tbobdy>
</table>






<h6># 操作串列用的方法函式</h6>

<table>
<thead>

<tr>
<th>方法使用</th>
<th>運算結果描述</th>
</tr>

</thead>

<tbody>

<tr>
<td>x.reverse()</td>
<td>反轉串列的順序</td>
</tr>

<tr>
<td>x.sort()</td>
<td>將串列的元素內容加以排序</td>
</tr>

<tr>
<td>x.pop()</td>
<td>彈出串列中最後一個元素</td>
</tr>


<tr>
<td>x.count(a)</td>
<td>計算x中出現的個數</td>
</tr>


</tbody>
</table>




<h6>#常用的內建函數</h6>
<table>

<thead>
<tr>
<th>函數名稱</th>
<th>使用說明</th>
</tr>
</thead>

<tbody>
<tr>
<td>range(a,b,c)</td>
<td>傳回a開始到b-1，間隔為c的序列數字</td>
</tr>

<tr>
<td>enumerate(x)</td>
<td>用列舉的方式，把迴圈進行中的索引值取出來</td>
</tr>
</tbody>

<tr>
<td>len(a)</td>
<td>計算變數a的長度，但a必需是可以計算長度的型態</td>
</tr>

<tr>
<td>sorted(a)</td>
<td>把a元素排序</td>
</tr>





</table>

<h6>#常用指令</h6>
<table>

<thead>
<tr>
<th>指令名稱</th>
<th>使用說明</th>
</tr>
</thead>

<tbody>
<tr>
<td>end=""</td>
<td>不換行</td>
</tr>

</table>


<h6>#語法</h6>

<ul>
<li>
<p>自訂函數</p>
<pre><code>
#1:
lambda 參數1,參數2, … : 敘述內容

Description:直接使用的行內無名函數,用完即丟自訂函數.<br>

#2：
def A(參數1,參數2):
    return 敘述內容 # return傳回去給呼叫的變數或對象 .

</code></pre>
</li>
</ul> 

