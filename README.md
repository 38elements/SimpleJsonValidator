SimpleJsonValidator
===================
Json形式のデータに対してスキーマを定義して型チェックを行なうプログラム。  
RedisやmemcacheでJsonを文字列で保存する際のチェックに用いる。
  
* スキーマの型はint, float, bool, str, list, dictのみを指定する。
* スキーマのintはint及びlongを許容する。
* スキーマのstrはstr及びunicodeを許容する。
* スキーマのlistは要素を1つのみ持つことができる。  
 (listの要素の型は1種類である。)
* スキーマと検証対象のデータのdictのキーは数や名称が一致していないと不正になる。
* 検証対象のデータにNone(null)があった場合は不正になる。
