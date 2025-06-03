# pyxel_testmode
## Pyxelの仕様テスト
 pyxel2.4.0で動作確認しています  

 以下のリンクからブラウザで動作確認することができます(一部機能は)
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
  loadによりパレットが変化することを確認します  
    img00.png  
    img01.png  
    img02.png  
  左右キーでimage02のみに00、01、02を順にloadします  

  それぞれ256x256のpngファイルです  
  イメージがloadされるとパレットが更新されます。(最大256色)  
  最後にloadしたイメージのカラーにパレットが更新されてしまいます  
  予めすべてのイメージに使用するカラーのpixelを登録しておくことで、load時の更新を抑制することができると考えています  
  最初の16色にはデフォルトのカラーをセットしています
  イメージ内で、未登録のカラーを使用しているとパレットの順がずれてしまいます
  
  
### 2:RELOAD 
  Aspriteを使用してイメージを編集することを想定しています  
    img_re00.png 

  Aspriteからイメージを保存してタイムスタンプが更新されるとreloadします  
  アニメーションパターンはプログラム内で定義しておく必要があります  

### 3:TILE 
  タイル表示のテスト  
  タイルマップは、my_resource.pyxres をloadします
  標準のリソースエディタで編集を想定しています  




