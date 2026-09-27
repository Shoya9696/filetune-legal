"""FileTune の法務・サポートページを作る（英語がルート、日本語は ja/）。

    python build.py

本文はこのファイルだけを直す。HTML は生成物（GitHub Pages でそのまま配信する）。
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
UPDATED_EN = "September 27, 2026"
UPDATED_JA = "2026年9月27日"
MAIL = "shoya96.apps@gmail.com"

CSS = """
    :root { color-scheme: light dark; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Hiragino Sans", "Noto Sans JP", sans-serif;
      line-height: 1.75; margin: 0; padding: 24px 16px 48px; background: #f7f8fa; color: #1a1a1a;
    }
    .container { max-width: 720px; margin: 0 auto; }
    .card { background: #fff; border: 1px solid #e2e6ee; border-radius: 12px; padding: 24px 20px; }
    h1 { font-size: 1.55rem; margin: 0 0 12px; }
    h2 { font-size: 1.15rem; margin: 28px 0 10px; border-bottom: 1px solid #e8ebf0; padding-bottom: 6px; }
    h3 { font-size: 1rem; margin: 18px 0 8px; }
    p, li { font-size: 0.96rem; }
    ul { padding-left: 1.2rem; }
    table { width: 100%; border-collapse: collapse; font-size: 0.92rem; margin: 12px 0; }
    th, td { border: 1px solid #dde2ea; padding: 8px 10px; text-align: left; vertical-align: top; }
    th { background: #f3f5f8; width: 28%; }
    .nav { margin-bottom: 16px; font-size: 0.9rem; }
    footer { margin-top: 24px; font-size: 0.85rem; color: #777; }
    a { color: #1a3f8f; }
    @media (prefers-color-scheme: dark) {
      body { background: #111318; color: #e8eaee; }
      .card { background: #1b1e25; border-color: #2c313b; }
      h2 { border-color: #2c313b; }
      th { background: #232833; }
      th, td { border-color: #2c313b; }
      a { color: #8fb4ff; }
      footer { color: #9aa0aa; }
    }
"""


def page(lang, title, body, footer):
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>{CSS}  </style>
</head>
<body>
  <div class="container">
{body}
    <footer>{footer}</footer>
  </div>
</body>
</html>
"""


# ---------------------------------------------------------------- English

EN_INDEX = f"""    <div class="card">
      <h1>FileTune</h1>
      <p>Support / Privacy Policy / Terms of Service</p>
      <p>FileTune converts files to another format on your iPhone or iPad, and can also finish them to meet conditions such as a size limit, a paper size, or a file name — then checks the finished file to show whether each condition was met. Everything is processed on your device.</p>
      <ul>
        <li><a href="support.html">Support</a></li>
        <li><a href="privacy-policy.html">Privacy Policy</a></li>
        <li><a href="terms-of-service.html">Terms of Service</a></li>
      </ul>
    </div>"""

EN_SUPPORT = f"""    <p class="nav"><a href="index.html">&larr; FileTune</a></p>
    <div class="card">
      <h1>Support</h1>
      <p>Help for "FileTune".</p>

      <h2>Contact</h2>
      <p>Email: <a href="mailto:{MAIL}">{MAIL}</a></p>
      <p>FileTune is developed by one person, so replies may take some time. Thank you for your patience.</p>
      <p>If a file does not convert as expected, it helps if you tell us the input format, the output format, the conditions you added, and your device and iOS version. Please do not send files that contain personal information.</p>

      <h2>FAQ</h2>

      <h3>What is free?</h3>
      <p><strong>Converting without conditions is free and unlimited.</strong> Conversions with conditions (size limit, paper size, file name, page count, quality, metadata) are free 3 times. After that, FileTune Pro — a one-time purchase, not a subscription — unlocks unlimited conversions with conditions. The price is shown on the purchase screen in the App.</p>
      <p>Only conversions that meet all of their conditions are counted. If a condition could not be met, that conversion is not counted.</p>

      <h3>Which formats are supported?</h3>
      <ul>
        <li>Input: PDF, JPEG, PNG, HEIC / HEIF, TIFF, BMP, GIF (first frame), WebP</li>
        <li>Output: PDF, JPEG, PNG, HEIC, TIFF, BMP</li>
      </ul>
      <p>Only formats your device can write are shown. Several photos can be combined into one PDF, and PDF pages can be exported as images.</p>

      <h3>The size limit could not be met</h3>
      <p>FileTune lowers the quality and, if needed, the resolution to fit the limit. When reaching the limit would make the images too degraded to be useful, it stops and tells you that the condition was not met. Try raising the limit, using fewer pages, or choosing JPEG instead of PNG.</p>
      <p>1 MB is counted as 1,000,000 bytes, so files also stay within limits that count 1 MB as 1,048,576 bytes.</p>

      <h3>My PDF cannot be converted</h3>
      <p>PDFs that are password-protected, or whose creator restricted copying or printing, cannot be converted. Please ask the creator for an unrestricted PDF.</p>

      <h3>Where are my converted files?</h3>
      <p>Use "Share" or "Save to Files" on the result screen. FileTune does not keep a library of converted files; they are removed when you start a new conversion. Your original files are never changed.</p>

      <h3>I purchased FileTune Pro, but conversions with conditions are still limited</h3>
      <p>Open "How to Use" (the ? button), tap FileTune Pro, and choose "Restore Purchase". This is needed after changing devices or reinstalling the App. Please make sure you are signed in with the same Apple Account you used for the purchase, and that you have a network connection.</p>
      <p>If you use "Ask to Buy", Pro is enabled automatically once the purchase is approved.</p>

      <h3>Do I need an account or an internet connection?</h3>
      <p>No account is needed. Conversion works offline. The only network access is to the App Store, for loading the price, purchasing, and restoring.</p>
    </div>"""

EN_PRIVACY = f"""    <p class="nav"><a href="index.html">&larr; FileTune</a></p>
    <div class="card">
      <h1>Privacy Policy</h1>
      <p>Last updated: {UPDATED_EN}</p>
      <p>This is the privacy policy for "FileTune" (the "App").</p>

      <h2>Information we collect</h2>
      <p><strong>The App does not collect any personal information, and never sends your files anywhere.</strong> The App does none of the following:</p>
      <ul>
        <li>Upload your files or their contents to a server</li>
        <li>Ask you to enter your name, email address, or similar information</li>
        <li>Access your location, contacts, camera, or microphone</li>
        <li>Obtain advertising identifiers (IDFA)</li>
        <li>Analyze how you use the App (analytics) or send crash reports to an outside service</li>
      </ul>
      <p>There is no account and no sign-in. We do not operate any server for the App.</p>

      <h2>Files you choose</h2>
      <p>The files and photos you choose are processed <strong>only on your device</strong>.</p>
      <ul>
        <li>Photos are chosen with the system photo picker. The App receives only the photos you select and cannot see the rest of your photo library.</li>
        <li>To convert, the App copies your files into its temporary working area on your device. <strong>Your original files are never changed.</strong></li>
        <li>Converted files stay in the temporary area until you share or save them. The working copies are deleted when you start a new conversion, and any left behind are cleaned up automatically.</li>
        <li>Photo information such as location and date taken (metadata) is kept or removed only as you choose with the metadata condition. The App does not read it for any other purpose.</li>
      </ul>

      <h2>Information stored on your device</h2>
      <table>
        <tr><th>Free conversions used</th><td>The number of free conversions with conditions you have used. Stored in the Keychain of this device only (it is not synced to other devices), so the count remains if you reinstall the App.</td></tr>
        <tr><th>Tip shown</th><td>Whether you have closed the first-launch tip.</td></tr>
        <tr><th>Purchase</th><td>Whether you have purchased FileTune Pro is managed by Apple (the App Store) and checked on your device.</td></tr>
      </table>
      <p>This information is never sent to us.</p>

      <h2>Network access</h2>
      <p><strong>The App connects to the network only for in-app purchase</strong>: when the FileTune Pro screen loads the price, when you purchase, and when you restore a purchase. The only party the App communicates with is Apple. Payments are processed by Apple, and we never receive your payment details.</p>
      <p>Converting files never uses the network. Everything except purchasing and restoring works in Airplane Mode.</p>

      <h2>Advertising and third parties</h2>
      <p>The App shows no ads and contains no advertising or analytics SDK. Because we collect nothing, there is no information to share with third parties.</p>

      <h2>Children</h2>
      <p>The App collects no personal information and has no way to interact with other users. Purchasing requires authentication with an Apple Account, and "Ask to Buy" is supported.</p>

      <h2>Changes</h2>
      <p>If this policy changes, the updated policy will be published on this page.</p>

      <h2>Contact</h2>
      <p>Please see the <a href="support.html">support page</a>.</p>
    </div>"""

EN_TERMS = f"""    <p class="nav"><a href="index.html">&larr; FileTune</a></p>
    <div class="card">
      <h1>Terms of Service</h1>
      <p>Last updated: {UPDATED_EN}</p>
      <p>These Terms set out the conditions for using "FileTune" (the "App"). By using the App, you agree to these Terms.</p>

      <h2>1. What is provided</h2>
      <p>The App converts files to another format on your device and can finish them to meet conditions such as a size limit, a paper size, a file name, a page count, a quality level, and metadata removal, then checks the finished file. Converting without conditions is free. Conversions with conditions are free 3 times; after that, they require FileTune Pro, an in-app purchase.</p>

      <h2>2. In-app purchase</h2>
      <ul>
        <li>Purchases are made through Apple's App Store, and payment is processed by Apple. The price is the amount shown on the purchase screen.</li>
        <li>FileTune Pro is non-consumable (a one-time purchase that stays valid). There is no subscription or recurring charge.</li>
        <li>After changing devices or reinstalling, you can recover your purchase with "Restore Purchase" in the App, using the same Apple Account.</li>
        <li>Refunds and billing matters follow Apple's policies and procedures.</li>
      </ul>

      <h2>3. Your files</h2>
      <p>Files are processed only on your device, and we never receive them. You are responsible for having the right to convert the files you use and for checking the results before you submit or share them. The App checks conditions on the finished file, but whether a file is accepted by a particular service is decided by that service.</p>

      <h2>4. Prohibited conduct</h2>
      <ul>
        <li>Decompiling, disassembling, or otherwise reverse-engineering the App</li>
        <li>Circumventing the purchase requirement by improper means</li>
        <li>Using the App to infringe the rights of others or in violation of applicable law</li>
      </ul>

      <h2>5. Intellectual property</h2>
      <p>Copyright and other rights in the App belong to us or their rightful owners. Files you convert remain yours.</p>

      <h2>6. Disclaimer</h2>
      <ul>
        <li>The App is provided "as is," without warranty of fitness for any particular purpose.</li>
        <li>We are not liable for damages arising from the use of, or inability to use, the App, except in cases of our willful misconduct or gross negligence.</li>
        <li>Please keep your original files. The App never changes them, but converted files are not kept after a new conversion starts.</li>
      </ul>

      <h2>7. Changes to or end of the App</h2>
      <p>We may change the contents of the App or stop providing it without prior notice. This does not prevent you from using the App already installed on your device.</p>

      <h2>8. Changes to these Terms</h2>
      <p>We may change these Terms. The changed Terms take effect when they are posted on this page.</p>

      <h2>9. Governing law and jurisdiction</h2>
      <p>These Terms are governed by the laws of Japan. Any dispute relating to the App shall be subject to the exclusive jurisdiction of the court having jurisdiction over our location as the court of first instance.</p>

      <h2>Contact</h2>
      <p>Email: <a href="mailto:{MAIL}">{MAIL}</a> (<a href="support.html">Support page</a>)</p>
    </div>"""

# ---------------------------------------------------------------- 日本語

JA_INDEX = f"""    <div class="card">
      <h1>FileTune（ファイルチューン）</h1>
      <p>サポート / プライバシーポリシー / 利用規約 / 特定商取引法に基づく表記</p>
      <p>FileTune は、ファイルを別の形式に変換し、必要なら「10MB以下」「A4」「ファイル名」などの条件に合わせて仕上げるアプリです。できたファイルを実際に確かめて、条件を満たしたかを見せます。処理はすべて端末の中で行います。</p>
      <ul>
        <li><a href="support.html">サポート</a></li>
        <li><a href="privacy-policy.html">プライバシーポリシー</a></li>
        <li><a href="terms-of-service.html">利用規約</a></li>
        <li><a href="commercial-disclosure.html">特定商取引法に基づく表記</a></li>
      </ul>
    </div>"""

JA_SUPPORT = f"""    <p class="nav"><a href="index.html">&larr; FileTune</a></p>
    <div class="card">
      <h1>サポート</h1>
      <p>「FileTune」のサポートページです。</p>

      <h2>お問い合わせ</h2>
      <p>メール: <a href="mailto:{MAIL}">{MAIL}</a></p>
      <p>個人で開発しているため、お返事に時間がかかることがあります。ご了承ください。</p>
      <p>うまく変換できないときは、元の形式・変換先・付けた条件・端末と iOS のバージョンを添えていただけると助かります。個人情報を含むファイルは送らないでください。</p>

      <h2>よくある質問</h2>

      <h3>無料で使える範囲は？</h3>
      <p><strong>条件なしの変換は、無料で何回でも使えます。</strong>条件（容量上限・用紙・ファイル名・ページ数・画質・メタデータ）を付けた変換は、無料で 3 回まで使えます。それ以降は、買い切りの「FileTune Pro」で条件つきの変換が無制限になります（サブスクではありません）。価格はアプリ内の購入画面に表示されます。</p>
      <p>回数に数えるのは、条件をすべて満たして完了した変換だけです。条件を満たせなかった変換は数えません。</p>

      <h3>対応している形式は？</h3>
      <ul>
        <li>読み込み: PDF・JPEG・PNG・HEIC / HEIF・TIFF・BMP・GIF（最初の1枚）・WebP</li>
        <li>書き出し: PDF・JPEG・PNG・HEIC・TIFF・BMP</li>
      </ul>
      <p>端末で書き出せる形式だけが表示されます。複数の写真を1つの PDF にまとめたり、PDF のページを画像にしたりできます。</p>

      <h3>容量上限を満たせなかった</h3>
      <p>画質と、必要なら解像度を下げて容量に合わせます。上限まで下げると画像が大きく劣化してしまう場合は、そこで止めて「満たしていません」とお知らせします。上限を増やす、ページ数を減らす、PNG ではなく JPEG にする、などをお試しください。</p>
      <p>1 MB は 1,000,000 バイトで数えます。提出先が 1 MB = 1,048,576 バイトで数えていても超えません。</p>

      <h3>PDF が変換できない</h3>
      <p>パスワードで保護された PDF や、作成者がコピー・印刷を制限している PDF は変換できません。制限のない PDF を作成者から受け取ってください。</p>

      <h3>変換したファイルはどこにある？</h3>
      <p>結果画面の「共有」または「ファイルに保存」で保存してください。FileTune は変換したファイルを一覧として保管せず、次の変換を始めると片付けます。元のファイルは変更しません。</p>

      <h3>FileTune Pro を購入したのに、条件つきの変換が制限される</h3>
      <p>「使い方」（？ボタン）→「FileTune Pro」→「購入を復元」をお試しください。機種変更や再インストールのあとに必要です。購入したときと同じ Apple アカウントでサインインしていること、インターネットにつながっていることもご確認ください。</p>
      <p>「承認と購入のリクエスト」をお使いの場合は、承認された時点で自動的に有効になります。</p>

      <h3>アカウントや通信は必要？</h3>
      <p>アカウントは不要です。変換は通信なしで使えます。通信するのは、価格の読み込み・購入・購入の復元で App Store とやりとりするときだけです。</p>
    </div>"""

JA_PRIVACY = f"""    <p class="nav"><a href="index.html">&larr; FileTune</a></p>
    <div class="card">
      <h1>プライバシーポリシー</h1>
      <p>最終更新日: {UPDATED_JA}</p>
      <p>「FileTune」（以下「本アプリ」）のプライバシーポリシーです。</p>

      <h2>収集する情報</h2>
      <p><strong>本アプリは個人情報を収集せず、ファイルを外部に送ることもありません。</strong>本アプリは次のことを一切行いません。</p>
      <ul>
        <li>ファイルやその内容をサーバーに送ること</li>
        <li>氏名・メールアドレスなどの入力を求めること</li>
        <li>位置情報・連絡先・カメラ・マイクへのアクセス</li>
        <li>広告識別子（IDFA）の取得</li>
        <li>利用状況の分析（アナリティクス）や、クラッシュレポートの外部送信</li>
      </ul>
      <p>アカウント・ログインはありません。本アプリのためのサーバーも運用していません。</p>

      <h2>選んだファイルの扱い</h2>
      <p>選んだファイルや写真は、<strong>端末の中だけで</strong>処理します。</p>
      <ul>
        <li>写真は iOS 標準の写真ピッカーで選びます。本アプリが受け取るのは選んだ写真だけで、写真ライブラリのほかの写真は見えません。</li>
        <li>変換のため、ファイルを端末内の一時的な作業領域に複製します。<strong>元のファイルは変更しません。</strong></li>
        <li>変換したファイルは、共有・保存するまで一時的な作業領域に置きます。次の変換を始めると作業用の複製は削除し、残ったものも自動で片付けます。</li>
        <li>写真の位置情報・撮影日時などの情報（メタデータ）は、メタデータの条件で選んだとおりに残すか削除するだけで、ほかの目的には使いません。</li>
      </ul>

      <h2>端末に保存する情報</h2>
      <table>
        <tr><th>無料の回数</th><td>条件つきの変換を無料で使った回数。この端末のキーチェーンにだけ保存します（ほかの端末とは同期しません）。アプリを入れ直しても残ります。</td></tr>
        <tr><th>案内の表示</th><td>初回の案内を閉じたかどうか。</td></tr>
        <tr><th>購入</th><td>FileTune Pro を購入したかどうかは Apple（App Store）が管理し、端末で確認します。</td></tr>
      </table>
      <p>これらの情報が運営者に送られることはありません。</p>

      <h2>通信</h2>
      <p><strong>本アプリが通信するのは、アプリ内課金のときだけです。</strong>FileTune Pro の画面で価格を読み込むとき、購入するとき、購入を復元するときに、Apple とだけ通信します。支払いは Apple が処理し、運営者が支払い情報を受け取ることはありません。</p>
      <p>ファイルの変換で通信することはありません。購入と復元以外は、機内モードでも使えます。</p>

      <h2>広告と第三者</h2>
      <p>本アプリは広告を表示せず、広告・分析の SDK も含みません。何も収集しないため、第三者に提供する情報もありません。</p>

      <h2>お子さまの利用</h2>
      <p>本アプリは個人情報を収集せず、ほかの利用者とやりとりする機能もありません。購入には Apple アカウントの認証が必要で、「承認と購入のリクエスト」に対応しています。</p>

      <h2>変更</h2>
      <p>このポリシーを変更する場合は、このページで公開します。</p>

      <h2>お問い合わせ</h2>
      <p><a href="support.html">サポートページ</a>をご覧ください。</p>
    </div>"""

JA_TERMS = f"""    <p class="nav"><a href="index.html">&larr; FileTune</a></p>
    <div class="card">
      <h1>利用規約</h1>
      <p>最終更新日: {UPDATED_JA}</p>
      <p>この規約は「FileTune」（以下「本アプリ」）の利用条件を定めるものです。本アプリを利用した時点で、この規約に同意したものとします。</p>

      <h2>1. 提供する内容</h2>
      <p>本アプリは、端末の中でファイルを別の形式に変換し、容量上限・用紙・ファイル名・ページ数・画質・メタデータの削除などの条件に合わせて仕上げ、できたファイルを確かめる機能を提供します。条件なしの変換は無料です。条件つきの変換は無料で 3 回まで使え、それ以降はアプリ内課金の「FileTune Pro」が必要です。</p>

      <h2>2. アプリ内課金</h2>
      <ul>
        <li>購入は Apple の App Store を通じて行い、支払いは Apple が処理します。価格は購入画面に表示される金額です。</li>
        <li>FileTune Pro は非消耗型（買い切り）です。サブスクリプションや継続的な課金はありません。</li>
        <li>機種変更や再インストールのあとは、同じ Apple アカウントでアプリ内の「購入を復元」から購入を戻せます。</li>
        <li>返金・請求に関する手続は、Apple の方針と手続に従います。</li>
      </ul>

      <h2>3. ファイルについて</h2>
      <p>ファイルは端末の中だけで処理し、運営者が受け取ることはありません。変換するファイルについて必要な権利を持っていること、提出・共有の前に仕上がりを確認することは、利用者の責任とします。本アプリはできたファイルで条件を確かめますが、提出先で受け付けられるかどうかは提出先が判断します。</p>

      <h2>4. 禁止事項</h2>
      <ul>
        <li>本アプリの逆コンパイル・逆アセンブルなどの解析</li>
        <li>不正な手段で購入の要件を回避すること</li>
        <li>他人の権利を侵害する目的や、法令に反する目的での利用</li>
      </ul>

      <h2>5. 知的財産</h2>
      <p>本アプリに関する著作権その他の権利は、運営者または正当な権利者に帰属します。変換したファイルは利用者のものです。</p>

      <h2>6. 免責</h2>
      <ul>
        <li>本アプリは現状のまま提供し、特定の目的への適合を保証しません。</li>
        <li>運営者の故意または重大な過失による場合を除き、本アプリの利用または利用できないことによる損害について責任を負いません。</li>
        <li>元のファイルは保管しておいてください。本アプリが元のファイルを変更することはありませんが、変換したファイルは次の変換を始めると残りません。</li>
      </ul>

      <h2>7. 内容の変更・提供の終了</h2>
      <p>運営者は、予告なく本アプリの内容を変更し、または提供を終了することがあります。提供を終了した場合でも、端末に入っている本アプリの利用を妨げるものではありません。</p>

      <h2>8. 規約の変更</h2>
      <p>運営者はこの規約を変更することがあります。変更後の規約は、このページに掲載した時点で効力を持ちます。</p>

      <h2>9. 準拠法・管轄</h2>
      <p>この規約は日本法に準拠します。本アプリに関する紛争は、運営者の所在地を管轄する裁判所を第一審の専属的合意管轄裁判所とします。</p>

      <h2>お問い合わせ</h2>
      <p>メール: <a href="mailto:{MAIL}">{MAIL}</a>（<a href="support.html">サポートページ</a>）</p>
    </div>"""

JA_DISCLOSURE = f"""    <p class="nav"><a href="index.html">&larr; FileTune</a></p>
    <div class="card">
      <h1>特定商取引法に基づく表記</h1>
      <p>FileTune</p>
      <table>
        <tr><th>サービス名</th><td>FileTune（ファイルチューン）</td></tr>
        <tr><th>事業者名</th><td>黒川翔哉</td></tr>
        <tr><th>事業者の住所・電話番号</th><td>住所・電話番号は、書面または電子メールによる請求があった場合に、購入の判断に先立ち遅滞なく提供します。<br>開示請求先: <a href="mailto:{MAIL}">{MAIL}</a></td></tr>
        <tr><th>問い合わせ先</th><td>メール: <a href="mailto:{MAIL}">{MAIL}</a><br>サポート: <a href="support.html">support.html</a></td></tr>
        <tr><th>販売価格</th><td>アプリ本体のダウンロードは無料です。条件なしの変換は無料で使えます。条件つきの変換は無料で 3 回まで使えます。<br>条件つきの変換を無制限にする「FileTune Pro」の日本国内価格は <strong>600円（税込）</strong>です。<br>実際の請求額・表示通貨・税込表示については、<strong>App Store（アプリ内）の購入画面の表示もあわせてご確認ください</strong>。地域・時期・Apple の表示仕様により、画面上の表記が異なる場合があります。</td></tr>
        <tr><th>商品以外の必要料金</th><td>購入および購入の復元にはインターネット接続が必要です。通信料は、お客様が契約する通信事業者が定める料金が発生する場合があります。<br>ファイルの変換に通信は不要です。</td></tr>
        <tr><th>支払方法</th><td>Apple の App Store を通じたアプリ内課金です。<br>お支払い手段は Apple アカウントに登録された方法に従い、Apple が処理します。運営者がクレジットカード番号などを取得・保管することはありません。</td></tr>
        <tr><th>支払時期</th><td>購入手続完了時に課金されます。<br>本商品は<strong>買い切りの非消耗型</strong>です。自動更新や追加の課金はありません。<br>「承認と購入のリクエスト」をご利用の場合、承認された時点で課金されます。</td></tr>
        <tr><th>役務の提供時期</th><td>購入手続が完了した時点から、条件つきの変換を回数の制限なくご利用いただけます。<br>反映に時間がかかる場合は、アプリ内の「購入を復元」をお試しください。</td></tr>
        <tr><th>返金について</th><td>返金・請求に関する手続は、<strong>Apple の返金・課金ポリシーおよび手続</strong>に従います。<br><a href="https://reportaproblem.apple.com/" rel="noopener noreferrer" target="_blank">Apple への返金請求はこちら</a></td></tr>
        <tr><th>動作環境</th><td>iOS 17.0 / iPadOS 17.0 以降の iPhone・iPad。購入・復元には App Store への接続が必要です。</td></tr>
      </table>
    </div>"""


def write(path, text):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8", newline="\n")


en_footer = lambda ja: f'FileTune &middot; <a href="{ja}">日本語</a>'
ja_footer = lambda en: f'FileTune &middot; <a href="{en}">English</a>'

write("index.html", page("en", "FileTune — Support and Legal", EN_INDEX, en_footer("ja/index.html")))
write("support.html", page("en", "FileTune — Support", EN_SUPPORT, en_footer("ja/support.html")))
write("privacy-policy.html", page("en", "FileTune — Privacy Policy", EN_PRIVACY, en_footer("ja/privacy-policy.html")))
write("terms-of-service.html", page("en", "FileTune — Terms of Service", EN_TERMS, en_footer("ja/terms-of-service.html")))
write("ja/index.html", page("ja", "FileTune — サポート・規約", JA_INDEX, ja_footer("../index.html")))
write("ja/support.html", page("ja", "FileTune — サポート", JA_SUPPORT, ja_footer("../support.html")))
write("ja/privacy-policy.html", page("ja", "FileTune — プライバシーポリシー", JA_PRIVACY, ja_footer("../privacy-policy.html")))
write("ja/terms-of-service.html", page("ja", "FileTune — 利用規約", JA_TERMS, ja_footer("../terms-of-service.html")))
write("ja/commercial-disclosure.html", page("ja", "FileTune — 特定商取引法に基づく表記", JA_DISCLOSURE, ja_footer("../index.html")))
write("README.md", """# FileTune — Support and legal pages

Support, privacy policy, terms of service, and (Japanese) commercial disclosure for the iOS / iPadOS app "FileTune".

- English: https://shoya9696.github.io/filetune-legal/
- 日本語: https://shoya9696.github.io/filetune-legal/ja/

The HTML is generated by `build.py`. Edit the text there and run `python build.py`.
""")
print("ok")
