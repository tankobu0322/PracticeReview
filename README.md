# 振り返りシートとは  
**TDU某G部**の練習終わりに書かされる手書きのレポートのこと  
手書きが故に時間的拘束が強く、全員書き終わるまで役員は帰れないとかいう鬼畜の所業  
少しでも負担を楽にしたいと思い作っているのが、その振り返りシートのwebアプリ版  

---

## 使用技術  
* HTML  
* Python  
* Django   
### Djangoを使ってみた理由
データベースをクラスとして簡単に定義できるので　　
HTMLベースでフォームを入力させるなら楽かなぁと考えたから。

---

## 使い方(できたとこまで)
とりあえずrunserverすると  
簡素なindexが表示される。  
![image](https://github.com/tankobu0322/PracticeReview/assets/170719141/9b07841e-3407-448e-ab04-e01ad893852d)  

投稿画面を開くと以下のような入力フォームが表示される  
![image](https://github.com/tankobu0322/PracticeReview/assets/170719141/12f58712-9084-448c-bce4-773a4f736c6a)  

データベースには以下のようなレコードが追加される  
![image](https://github.com/tankobu0322/PracticeReview/assets/170719141/1750ec8f-d718-41ff-bd9e-63c75f501722)  

---
### 今後実装する機能  
* 外部キー, 複数テーブル定義  
* ログイン認証  
* bootstrapとbase.htmlで簡単に見た目を統一, 良いwebデザインを作りたい  

