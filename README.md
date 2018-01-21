# Marking_Words

###### 因为背单词书实在太枯燥，就想着边读文章边背单词。但是英文原版书里不认识的单词太多，很多并不是常用词汇，所以就想把文章里出现的单词书里的单词出来，方便在一个语境下背诵。

##### 例子：在Kindle里点击`[i]`，下方会弹出注释。注释来源于单词书
![](https://github.com/2918diy/Marking_Words/blob/master/screenshot_2018_01_21T13_00_37%2B0800.jpg)

##### 文件素材：
* 经济学人半年刊中英双语 Epub电子书
* GMAT和TOFEL的红宝书 Epub电子书

##### 步骤：
* 先把经济学人的电子书解压，Epub可以直接用任何解压软件解压为一个文件夹。在其中的一个文件夹里放着很多Html文件。电子书里的每篇文章就是以Html文件格式储存的。
* 把GMAT和TOFEL的红宝书解压，然后提取出里面的单词和释义，导出为csv文件。（参见另一个Repository)
* 按照上述文件的文件路径修改 `word_note.py`文件里的文件路径，运行。

##### 代码思路：
* 遍览解压后电子书文件夹里的所有文件，找到记录着文章的文件加入列表
* 读取csv文件里的单词，并根据每一个单词做一个注释tag（`<aside></aside>`）
* 遍览所有文章HTML文件，读取并建立BeautifulSoup对象。用文章中出现过的英文单词建立这篇文章的单词字典。
* 将文章里的单词表和单词书的单词表进行比较。
* 将重合的单词替换为带注释的HTML Tag
