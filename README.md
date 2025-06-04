# pyxel_testmode
## Pyxelの仕様テスト
 pyxel2.4.0で動作確認しています  

 以下のリンクからブラウザで動作確認することができます(RELOADなど一部機能は確認できません)    
 [PyxelTestMode](https://kitao.github.io/pyxel/wasm/launcher/?play=mkmk2.PyxelTestMode.src.PyxelTestMode&gamepad=enabled)


 0:COLOR  
 1:IMG LOAD  
 2:RELOAD  
 3:TILE  

  上下キーでメニュー選択  
  スクリーン左側のパレットは常時表示  

### 0:COLOR
  現在のパレットを表示

### 1:IMG LOAD 
  pyxel.image.loadを使用してイメージファイルをloadします  
  ゲームの途中(シーンの切り替わりではなく、ゲームの途中)でimageを更新したい時に使う想定です  
  loadによりパレットが変化する(変化しない)ことを確認します  
    img00.png  
    img01.png  
    img02.png  
  左右キーでimage02のみに00、01、02を順にloadします  

  それぞれ256x256のpngファイルです  
  load時、incl_colors=True を指定することで、そのpngファイルで使用されているカラーをパレットに取り込みます(最大256色)  
  このとき、最後にloadしたイメージのカラーにパレットが更新されてしまいます  
  予めすべてのイメージに使用するカラーを登録しておくことで、load時のパレット更新を抑制することができると考えています  
  02にload後も、00、01のimageが変化しないことが確認できます  
  ただし、02のload時にちらつきが見られることがあるので、loadはそのimageを利用していないタイミングに行うのが良いようです  

### 2:RELOAD 
  Aspriteを使用してイメージを編集することを想定しています  
    img_re00.png 

  Aspriteからイメージを保存してタイムスタンプが更新されるとreloadします  
  アニメーションパターン(u、vやサイズなど)はプログラム内で定義しておく必要があります  

### 3:TILE 
  タイル表示のテスト  
  タイルマップは、my_resource.pyxres をloadします
  標準のリソースエディタで編集を想定しています  




