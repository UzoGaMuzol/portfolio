from flask import jsonify, url_for, Blueprint

blueprint = Blueprint(
    "api",
    __name__,
    url_prefix = "/api"
)

@blueprint.route("/")
def index():
    data = {
        "name": {
            "jp": "ウゾガムゾル",
            "en": "Uzo Ga Muzol",
        },
        "another_name": {
            "jp": "脛孝行",
            "en": "sune_koko"
        },
        "real_name": {
            "jp": "不明",
            "en": "Unknown"
        },
        "other_names": [
            "Sponge Of Parents"
        ],
        "gender": "he/him",
        "occupation": "大学生",
        "genres": [
            "ボカロP",
            "動画投稿者",
            "小説執筆",
            "プログラミング"
        ],
        "hobbies": [
            "音楽を聴くこと",
            "作曲",
            "ネットサーフィン",
            "PCゲーム"
        ],
        "links": {
            "Twitter_main": "https://twitter.com/uzogamuzol",
            "YouTube_main": "https://www.youtube.com/channel/UCsE5FbMXnmBYe-THSt3kwJQ",
            "YouTube_sub": "https://www.youtube.com/c/sune_koko",
            "NicoNico": "https://nicovideo.jp/user/46928394",
            "Sound Cloud": "https://soundcloud.com/uzogamuzol",
            "Piapro": "https://piapro.jp/icchy1128music",
            "Kakuyomu": "https://kakuyomu.jp/users/icchy1128Novelman",
            "GitHub": "https://github.com/UzoGaMuzol"
        }
    }
    return jsonify(data)

@blueprint.route("/career")
def career():
    data = {
        "小学校まで": ("落ち着きのない子供だった。見知らぬ人とすぐに話せたが、"
            "一方で特定のグループに属さず渡り歩いていたり、"
            "クラスが変わった友達と関わらなくなるなど仲を深められない一面もあった。"
            "片思いの失敗や嫌がらせ、友人関係の些細なトラウマなどにより徐々に心を閉ざしていく。"
            "そんな中うごくメモ帳3Dをきっかけにネットに触れ始め、ニコニコ動画やYouTubeを見始める。"),
        "中学校・高校": ("中学に入る辺りで本格的にネットを見るようになった。"
            "SNSよりもどちらかというと古いアングラなサイトを好む。"
            "カゲロウプロジェクトを始めとするボーカロイドにハマったり、"
            "クラスのオタクグループに近づくようになったがそこにも入りこみ切れず。"
            "部活等で息苦しい日々を送り、さらなる片思いの失敗もありさらに心が暗くなっていく。"
            "高校受験のやる気は皆無であり、親に進められるままの高校を受験し合格。"
            "高校では軽音部に入り、洋楽ロックと出会う。"
            "バンドを組んで自分やメンバーの作った曲をライブで演奏したりした。"
            "ロックは音楽性のみならず価値観にも影響を与えた。"
            "しかし再び片思いに失敗したことにより完全に自信喪失し、"
            "「クラスの変な人」から「クラスの隅のぼっち」へと転落した。"
            "但しその後文化祭のライブでわずかに持ち直す。"
            "ボカロ曲の投稿を始めたのはこの頃である。ただし再生数はYouTube、ニコニコ共に500未満がほとんどであった。"
            "3年生でブログを始める（後に恥ずかしくなり閉鎖）。収益などはなかった。"
            "大学受験も例によってやる気がなく、センター真っ只中の冬に曲を投稿するなどしていたが、"
            "某私大に（奇跡的に？）合格。"),
        "大学生": ("コロナの影響で全講義がリモートという状況から始まった。"
            "授業以外活動的なこと（バイト・サークル・免許取得・友人との交遊）を一切しないという堕落した生活を送る。"
            "情報系の学部ということもあり技術に興味が出始め、PCを購入しBlenderやUnityなどで遊び始める。"
            "Pink FloydやBlack Sabbathといった最も好きなバンドに出会うが、"
            "高校時代にやっていたようなバンド活動などは行わず、家に引きこもる。"
            "また作曲頻度が落ちる。その代わりに小説等を執筆していたが頓挫。"
            "3年からVOICEVOXに出会いサブチャンネルでずんだもん動画を投稿し始める。"
            "うごメモ3D時代から続いた「自分の作品が人に見られない」状況が打破されたが、"
            "プレッシャーと迷い、再生数の低下もあって現在は余り投稿出来ていない。"
            "一方YouTubeに投稿した曲「沈んでゆく」が1200回以上再生され、"
            "他の曲にも絶賛のコメントが来るなど、わずかな希望が見えなくもないという状況である。")
    }
    return jsonify(data)

@blueprint.route("/music")
def music():
    data = {
        "concept": ("ウゾガムゾルは、"
            "「取るに足らない多くの事物」を意味する四字熟語「有象無象」に由来する。"
            "初音ミクをはじめとする歴史あるボーカロイド達と共に、"
            "現代の絶望・悲しみ・怒りを、ときに鋭く、ときにやんわりと表現する。"
            "ハード・ロック、プログレッシブ・ロック、"
            "オルタナティブ・ロックなどの影響を昇華させながら、独自の音楽を構築する。"),
        "description": ("YouTubeを中心に楽曲を投稿。2019年4月に投稿開始。"
            "音楽性は暗い・激しいものが多いが、そうでないものもある。"
            "歌詞のテーマは、失恋（一部）、厭世、怒り、風刺。"),
        "projects": [
            {
                "name": "From The Sickroom",
                "type": "Album",
                "concept": "暗い病院にて、死にかけの少年と死にたい少女が邂逅する──。",
                "description": ("オリジナルアルバム。間は開くが制作期間は4年ほど。"
                    "GarageBandで作った実験的な曲を集めるというコンセプトだったが、"
                    "最終曲「Botanical Body In Sanatorium」のアイデアを思いついてからは"
                    "厭世と絶望とその末路を表現することを主軸とした。"
                    "6「The Zombie Disease」と12「Botanical Body In Sanatorium」"
                    "のみCubaseで制作。それ以外はGarageBand製。"),
                "link": "https://www.youtube.com/watch?v=2HWfb-UgwdE"
            },
            {
                "name": "ム　～いのちの見た夢～",
                "type": "Album, Media Mix Project",
                "concept": "心に闇を抱えた、6人の少女たちの世界。生まれて、死んで、審判を繰り返し、最後に行きつく先とは。",
                "description": ("オリジナルアルバムを中心とするメディアミックスプロジェクト。"
                    "アルバム、ゲーム、小説で展開する予定。現在も制作中である。"
                    "アルバムは3枚組予定。ゲームはゆめにっき派生の形式。小説はカクヨムに投稿。"
                    "日々に疲れた大学生。虐待に苦しむ過去を持つ者。狼少女として生まれた者。"
                    "戦争に巻き込まれた少女。未曽有の殺人鬼となった少女。"
                    "これら6人が織りなす絶望と破滅の物語。"),
                "link": "https://www.youtube.com/playlist?list=PLXwf_yDfnR8PP8EBZz5u7RgaKXHFNgEkE"
            }
        ]
    }
    return jsonify(data)

@blueprint.route("/others")
def others():
    data = {
        "description": "音楽以外にもいろいろな活動をしてきた。",
        "projects": [
            {
                "name": "永遠のゆく先へ",
                "type": "Novel",
                "concept": ("多感な女子高生3人と、空から降ってきた謎の少女の"
                    "4人が繰り広げる、冒険SF物語！"),
                "description": ("青春SFストーリー。現在2話まで。"),
                "link": "https://kakuyomu.jp/works/1177354054897407929"
            },
            {
                "name": "インフォメーション・ガール",
                "type": "Novel",
                "concept": ("全世界のコンピューターに出現し始めた謎の少女……。"
                    "フレンドリーだが、人間の体を乗っ取って自らのファンアートを書かせる、"
                    "SNSの裏垢で過激な投稿をするなどの一面も。"
                    "彼女の動向と、闇に包まれた過去とは。"),
                "description": ("断片的な資料を読みながら真相に迫っていく形式の小説。"
                    "アバターを着て活動する者たちと人工知能、人の感情とその末路。"
                    "補足資料としてVRoid Hubにアバターを投稿している。"
                    "https://hub.vroid.com/users/26489552"),
                "link": "https://kakuyomu.jp/works/16816700429270231685"
            }
        ]
    }
    return jsonify(data)

@blueprint.route("/as_sune_koko")
def as_sune_koko():
    data = {
        "link": "https://www.youtube.com/c/sune_koko",
        "description": ("もともとボカロ曲に関係ない動画を投稿するために"
            "作った「ウゾガムゾルのサブチャンネル」だったが、"
            "ある時からミーム動画を投稿し始め、「脛孝行」に改名する。"
            "その後VOICEVOXを知ったことをきっかけにずんだもんを使った"
            "ふざけた動画を投稿し始める。"),
        "works": [
            {
                "name": "【VOICEVOX劇場】春休み大学生ずんだもんの一日【ニート】",
                "link": "https://youtu.be/n55ka3UFgBk",
                "description": "最初に作ったずんだもん動画。完全に自分語りであるため特筆することはない。"
            },
            {
                "name": "ゲーミングずんだもん",
                "link": "https://youtu.be/dRT8ilMXkgg",
                "description": ("初めて伸びた動画。ずんだもんが7色に光るだけの7秒動画だが、"
                    "現在最高記録である12万回再生を記録。")
            },
            {
                "name": "誰でも試せる!! 群れになって泳ぐずんだもんのアプリをリリース！！",
                "link": "https://youtu.be/c1_cPFPSIfw",
                "description": ("以前投稿していた「boidモデルを使ってずんだもんを群れにした動画」を、"
                    "P5.jsで実装したという動画。https://zunda-boid.web.app/"
                    "このサイトを共有したツイート（自分のではない）が公式にRTされた模様。")
            },
            {
                "name": "【VOICEVOX劇場】4630万ずんだを誤送付されたずんだもん",
                "link": "https://youtu.be/VeL_GEJUaqQ",
                "description": "時事ネタ。群れになって泳ぐずんだもんをオチに使用した。"
            },
            {
                "name": "ヘコワープ",
                "link": "https://youtu.be/zp2kRWD4rmA",
                "description": ("突然流行ったミームをマリオ64のケツワープと悪魔合体させたという"
                    "出オチ動画。ゲーミングずんだもんに次ぐ10万再生を記録。")
            },
            {
                "name": "ずんだもんであそぼう",
                "link": "https://youtu.be/QuDWCQTPESo",
                "description": ("「○○であそぼう」を踏襲した動画。"
                    "Google翻訳の声ではなくずんだもんを使用している。")
            },
            {
                "name": "ずんだもんBB?+使用例",
                "link": "https://youtu.be/6mlA3WQNhz8",
                "description": "ずんだもんが出てくる動画。"
            },
            {
                "name": "ずんだもんと学ぶ小便器の正しいマナー",
                "link": "https://youtu.be/q0vFZ0zrOzg",
                "description": "Urinal Etiquetteという海外ミームのパロディ。"
            }
        ]
    }
    return jsonify(data)