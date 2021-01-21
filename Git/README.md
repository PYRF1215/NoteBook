# <h2>●Git 版本管理</h2>
[![Git 版本管理](https://github.com/PYRF1215/Classification/blob/master/Git/images/%E9%A6%96%E9%A0%81.png)](https://www.youtube.com/watch?v=NugoF40e6Dk)    



# 
<ul>
  <li>
  <p>影片大網</p>
  <ul>
  <li>Git前置作業 10:30</li>
  <li>建立軟體專案 19:50 </li>
  <li>建立新版本 27:00 </li>
  <li>GitHub 雲端專案管理 33:00 </li> 
  <li>團體開發 43:10</li> 
  <li>流程示意圖 1:10:10</li> 
  <li>Discussion 1:18:30</li>   
  </ul>
  </li>
</ul>

# <h2>●前置作業</h2>
download : https://git-scm.com  
install ： All default

# <h2>●個人管理</h2>
<pre><code>
git init // 初始化
git status // 觀看狀態
git add . // 加入追縱
git commit -m "First Commit" // 建立新版本
git log // 版本記錄
</code></pre>

  
# <h2>●團體專案開發管理</h2>  
<pre><code>
git remote -v //觀看有無關連遠端空間 (加入關連只需做一次)  
git remote add origin https://github.com/YCHsu8327/test.git  
D:\Program\GitHub\git\b0909182697\project-1>git remote -v  

git clone url project-2 // 下載GitHub雲端專案()
git pull origin master  // 將GitHub雲端最新專案檔案拉下來 (僅拉下更新部份)
write code // 寫程式
git status  // 觀看資料狀態
git commit -m "Modified code" // 建立新版本 
git push origin master  //  將local端資料上傳至GitHub團體開發區 (更新專案檔案)
</code></pre>


# <h2>●無法git push origin master</h2>
<pre><code>
error msg : The requested URL returned error: 403

.git/config

[remote "origin"]
	url = https://github.com/b0909182697/YC.git  

修改成↓

[remote "origin"]
	url = https://b0909182697@github.com/b0909182697/YC.git

Authentication Succeeded 重新認證即可.
</code></pre>



# <h2>●無法推送異常處理</h2>
<pre><code>
error msg : 

git fetch origin master
git merge origin master

git fetch origin master:tmp
git rebase tmp
git push origin HEAD:master
git branch -D tmp
</code></pre>


