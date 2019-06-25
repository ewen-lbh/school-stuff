module.exports = {

  onWillParseMarkdown: function (markdown) {
    return new Promise((resolve, reject) => {

      schoolsystKaTeX_escapes = [
        '{','}','(',')','$', '>', '<'
      ]

      schoolsystKaTeX_color_names = {
        mx3creations: "#268cce"
      }

      // an array of a [search,replace] arrays, with regular strings (_strings) or regex patterns (_regex, _regex_2vars, _regex_4vars)
      // replacing is done in the array's order.
      // for _autobackslashes, it's an array of strings that are to be replaced according to : .tring => string
      schoolsystKaTeX_regex = [
        [/ vec (.)/g, '\\vec{$1}'],
        [/ bar (.)/g, '\\bar{$1}'],
        [/ (?:~|tilde)\(([^)]+)\)/g, "\\widetilde{$1}"],
        [/ group\(([^)]+)\)/g, "\\overgroup{$1}"],
        [/ ugroup\(([^)]+)\)/g, "\\undergroup{$1}"],
        [/ vec\(([^)]+)\)/g, "\\vec{$1}"],
        [/ (?:\^\^|hat|angle)\(([^)]+)\)/g, "\\widehat{$1}"],
        [/ bar\(([^)]+)\)/g, "\\bar{$1}"],
        [/ ceil (.)/g, "\\lceil $1 \\rceil"],
        [/ floor (.)/g, "\\lfloor $1 \\rfloor"],
        [/ ceil\(([^)]+)\)/g, "\\left \\lceil $1 \\right \\rceil"],
        [/ floor\(([^)]+)\)/g, "\\left \\lfloor $1 \\right \\rfloor"],
        [/ \( ([^)]+) \)/g, "\\left ( $1 \\right )"],
        [/ \{ ([^)]+) \}/g, "\\left \\{ $1 \\right \\}"],
        [/ \|\| \(([^)]+)\) \|\|/g, "\\left \\Vert $1 \\right \\Vert"],
        [/ \| \(([^)]+)\) \|/g, "\\left \\vert $1 \\right \\vert"],
        [/ (?:Rs|reals|réels)/g, "\\R"],
        [/ (?:Re|real|réel)/g, "\\Re"],
        [/ (?:Zs|integers|entiers)/g, "\\Z"],
        [/ (?:Ns|naturals|naturels)/g, "\\N"],
        [/ (?:Cs|complexs|complexes)/g, "\\Complex"],
        [/ ([+\-]?)oo/g, "$1\\infty"],
        [/ f"([^"]+)"/g, "\\mathcc{$1}"],
        [/ o"([^"]+)"/g, "\\mathbb{$1}"],
        [/ b"([^"]+)"/g, "\\mathbf{$1}"],
        [/ s"([^"]+)"/g, "\\mathsf{$1}"],
        [/ k"([^"]+)"/g, "\\mathfrak{$1}"],
        [/ n"([^"]+)"/g, "\\text{$1}"],
        [/ [mt]"([^"]+)"/g, "\\mathtt{$1}"],
        [/ del (.)/g, "\\cancel{$1}"],
        [/ del\(([^)]+)\)/g, "\\sout{$1}"],
        [/ \[\[ ([^\]]) \]\]/g, "\\boxed{$1}"],
        [/ box\{([^\]])\}/g, "\\boxed{$1}"],
        [/ <([^>])>/g, "\\tag{$1}"],
        [/ (?:union|cup) /g, "\\cup "],
        [/ (?:inter|cap) /g, "\\cap "],
        [/ (?:Union|Cup) /g, "\\Cup "],
        [/ (?:Inter|Cap) /g, "\\Cap "],
        [/ (?:sqrt|root) (?:of )?(.)/g, "\\sqrt{$1}"],
        [/ (?:sqrt|root)\((.+)\)/g, "\\sqrt{$1}"],
        [/ !(.+) /g, "\\not $1 "],
        [/ \?(.+)/g, "\\stackrel{?}{$1}"],
        [/ (.+)\? /g, "\\stackrel{?}{$1}"],
      ]
      //
      schoolsystKaTeX_regex_2vars = [
        [/note"([^"]+)"\{(.+)\}/g, "\\underbrace{$2}_{\\mathclap{\\text{$1}}}"],
        [/note\{(.+)\}"([^"]+)"/g, "\\underbrace{$1}_{\\mathclap{\\text{$2}}}"],
        [/forall (.+) in (.+) /g, "\\forall \\; $1 \\in $2 \\quad"],
        [/#([A-Fa-f0-9]{3,6})\{(.+)\}/g, "\\color{#$1}{$2}"],
        [/sum (?:from )?(.+) to (.+) /g, "\\sum _{\\mathclap{$1}}^{\\mathclap{$2}}"],
        [/prod(?:uct)? (?:from )?(.+) to (.+) /g, "\\prod _{\\mathclap{$1}}^{\\mathclap{$2}}"],
        [/coprod(?:uct)? (?:from )?(.+) to (.+) /g, "\\coprod _{\\mathclap{$1}}^{\\mathclap{$2}}"],
        [/(?:union|cup) (?:from )?(.+) to (.+) /g, "\\cup _{\\mathclap{$1}}^{\\mathclap{$2}}"],
        [/(?:inter|cap) (?:from )?(.+) to (.+) /g, "\\cap _{\\mathclap{$1}}^{\\mathclap{$2}}"],
        [/ ([^/}])\/([^/}])/g, "\\frac{$1}{$2}"],
        [/ \(([^)}]+)\)\/\(([^)}]+)\)/g, "\\frac{$1}{$2}"],
        [/ \((.);(.)\)/g, "\\binom{$1}{$2}"],
        [/ (.)(?:th|st|nd|rd) (?:sqrt|root) (?:of )?(.)/g, "\\sqrt[$1]{$2}"],
        [/ (.)(?:th|st|nd|rd) (?:sqrt|root)\((.+)\)/g, "\\sqrt[$1]{$2}"],
        [/ \((.+)\)(?:th|st|nd|rd) (?:sqrt|root) (?:of )?(.)/g, "\\sqrt[$1]{$2}"],
        [/ \((.+)\)(.)(?:th|st|nd|rd) (?:sqrt|root)\((.+)\)/g, "\\sqrt[$1]{$2}"],
      ]
      //
      // schoolsystKaTeX_regex_4vars = [
      //   [/(o?)(i{1,3})nt(?:egral)? (?:from )?(.+) to (.+) /g, "\\$1$2nt _{$3}^{$4}"],
      // ]
      schoolsystKaTeX_autobackslash = "alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda mu nu xi pi rho sigma tau upsilon phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Phi Psi Omega sum bigotimes bigvee bigoplus bigwedge bigodot bigcap bigcup biguplus mod cos arcos sin arcsin tan arctan arctg arcctg arg ch cosec cosh cot argmin cotg coth csc ctg cth deg dim exp hom ker lg ln log sec sinh sh tan tanh tg th det gcd inf lim liminf limsup max min Pr sup argmax oplus ominus log ast  forall subset superset in".split(' ')
      schoolsystKaTeX_strings = [
        [' * ', '\\cdot'],
        [' |-> ', '\\mapsto '],
        [' --> ', '\\to '],
        [' <-- ', '\\gets '],
        [' <-> ', '\\leftrightarrow '],
        [' ==> ', '\\implies '],
        [' <== ', '\\impliedby '],
        [' <=> ', '\\iff '],
        [' and ', '\\land '],
        [' or ', '\\lor '],
        [' not ', '\\lnot '],
        [' empty', '\\emptyset'],
        [' nothing', '\\varnothing'],
        [' +- ', '\\pm '],
        [' -+ ', '\\mp '],
        [' // ', ' / '],
        [' \\\\ ', '\\setminus '],
        [' \\ ', '\\smallsetminus '],
        [' xx ', '\\times '],
        [' .> ', '\\gtrdot '],
        [' <. ', '\\lessdot'],
        [' .+ ', '\\dotplus '],
        [' && ', '\\And '],
        [' ~ ', '\\sim '],
        [' ~= ', '\\simeq '],
        [' ~~ ', '\\approx '],
        [' == ', '\\equiv '],
        [' o= ', '\\eqcirc '],
        [' >= ', '\\geqslant '],
        [' <= ', '\\leqslant '],
        [' >=< ', '\\lesseqgtr '],
        [' >< ', '\\lessgtr '],
        [' <> ', '\\lessgtr '],
        [' -: ', '\\eqcolon '],
        [' -:: ', '\\Eqcolon '],
        [' =: ', '\\eqqcolon '],
        [' =:: ', '\\Eqqcolon '],
        [' :: ', '\\dblcolon '],
        [' .= ', '\\doteq '],
        [' .=. ', '\\Doteq '],
        [' _|_ ', '\\bot '],
      ]

      // var decodeHtmlEntity = function(str) {
      //   return str.replace(/&#(\d+);/g, function(match, dec) {
      //     return String.fromCharCode(dec);
      //   });
      // };

      // var encodeHtmlEntity = function(str) {
      //   var buf = [];
      //   for (var i=str.length-1;i>=0;i--) {
      //     buf.unshift(['&#', str[i].charCodeAt(), ';'].join(''));
      //   }
      //   return buf.join('');
      // };

      // function colourNameToHex(colour)
      // {
      //     var colours = {"aliceblue":"#f0f8ff","antiquewhite":"#faebd7","aqua":"#00ffff","aquamarine":"#7fffd4","azure":"#f0ffff",
      //     "beige":"#f5f5dc","bisque":"#ffe4c4","black":"#000000","blanchedalmond":"#ffebcd","blue":"#0000ff","blueviolet":"#8a2be2","brown":"#a52a2a","burlywood":"#deb887",
      //     "cadetblue":"#5f9ea0","chartreuse":"#7fff00","chocolate":"#d2691e","coral":"#ff7f50","cornflowerblue":"#6495ed","cornsilk":"#fff8dc","crimson":"#dc143c","cyan":"#00ffff",
      //     "darkblue":"#00008b","darkcyan":"#008b8b","darkgoldenrod":"#b8860b","darkgray":"#a9a9a9","darkgreen":"#006400","darkkhaki":"#bdb76b","darkmagenta":"#8b008b","darkolivegreen":"#556b2f",
      //     "darkorange":"#ff8c00","darkorchid":"#9932cc","darkred":"#8b0000","darksalmon":"#e9967a","darkseagreen":"#8fbc8f","darkslateblue":"#483d8b","darkslategray":"#2f4f4f","darkturquoise":"#00ced1",
      //     "darkviolet":"#9400d3","deeppink":"#ff1493","deepskyblue":"#00bfff","dimgray":"#696969","dodgerblue":"#1e90ff",
      //     "firebrick":"#b22222","floralwhite":"#fffaf0","forestgreen":"#228b22","fuchsia":"#ff00ff",
      //     "gainsboro":"#dcdcdc","ghostwhite":"#f8f8ff","gold":"#ffd700","goldenrod":"#daa520","gray":"#808080","green":"#008000","greenyellow":"#adff2f",
      //     "honeydew":"#f0fff0","hotpink":"#ff69b4",
      //     "indianred ":"#cd5c5c","indigo":"#4b0082","ivory":"#fffff0","khaki":"#f0e68c",
      //     "lavender":"#e6e6fa","lavenderblush":"#fff0f5","lawngreen":"#7cfc00","lemonchiffon":"#fffacd","lightblue":"#add8e6","lightcoral":"#f08080","lightcyan":"#e0ffff","lightgoldenrodyellow":"#fafad2",
      //     "lightgrey":"#d3d3d3","lightgreen":"#90ee90","lightpink":"#ffb6c1","lightsalmon":"#ffa07a","lightseagreen":"#20b2aa","lightskyblue":"#87cefa","lightslategray":"#778899","lightsteelblue":"#b0c4de",
      //     "lightyellow":"#ffffe0","lime":"#00ff00","limegreen":"#32cd32","linen":"#faf0e6",
      //     "magenta":"#ff00ff","maroon":"#800000","mediumaquamarine":"#66cdaa","mediumblue":"#0000cd","mediumorchid":"#ba55d3","mediumpurple":"#9370d8","mediumseagreen":"#3cb371","mediumslateblue":"#7b68ee",
      //     "mediumspringgreen":"#00fa9a","mediumturquoise":"#48d1cc","mediumvioletred":"#c71585","midnightblue":"#191970","mintcream":"#f5fffa","mistyrose":"#ffe4e1","moccasin":"#ffe4b5",
      //     "navajowhite":"#ffdead","navy":"#000080",
      //     "oldlace":"#fdf5e6","olive":"#808000","olivedrab":"#6b8e23","orange":"#ffa500","orangered":"#ff4500","orchid":"#da70d6",
      //     "palegoldenrod":"#eee8aa","palegreen":"#98fb98","paleturquoise":"#afeeee","palevioletred":"#d87093","papayawhip":"#ffefd5","peachpuff":"#ffdab9","peru":"#cd853f","pink":"#ffc0cb","plum":"#dda0dd","powderblue":"#b0e0e6","purple":"#800080",
      //     "rebeccapurple":"#663399","red":"#ff0000","rosybrown":"#bc8f8f","royalblue":"#4169e1",
      //     "saddlebrown":"#8b4513","salmon":"#fa8072","sandybrown":"#f4a460","seagreen":"#2e8b57","seashell":"#fff5ee","sienna":"#a0522d","silver":"#c0c0c0","skyblue":"#87ceeb","slateblue":"#6a5acd","slategray":"#708090","snow":"#fffafa","springgreen":"#00ff7f","steelblue":"#4682b4",
      //     "tan":"#d2b48c","teal":"#008080","thistle":"#d8bfd8","tomato":"#ff6347","turquoise":"#40e0d0",
      //     "violet":"#ee82ee",
      //     "wheat":"#f5deb3","white":"#ffffff","whitesmoke":"#f5f5f5","yellow":"#ffff00","yellowgreen":"#9acd32"};

      //     colors = Object.assign({}, coulours, schoolsystKaTeX_color_names)

      //     if (typeof colors[colors.toLowerCase()] != 'undefined')
      //         return colors[colors.toLowerCase()];

      //     return '#000000';
      // }



      // /* ----------------
      //       MARKDOWN
      // --------------- */

      // Underlined text: __text__ => <u>text</u>
      markdown = markdown.replace(/__(.+)__/gm, ($0, $1) => '<u>' + $1 + '</u>')
      // // Newline (might remove): \n => <br>
      // markdown = markdown.replace(/\\n(.)/gm, ($0, $1) => '<br>' + $1)

      // // Dotted arrows
      // markdown = markdown.replace('...>','···>')
      // markdown = markdown.replace('..>','··>')

      // Special arrows
      markdown = markdown.replace(/\|_>/g,  $0 => '↳')
      markdown = markdown.replace(/\/\^/g , $0 => '↗')
      markdown = markdown.replace(/\\\^/g , $0 => '↘')



      // // Named headers: #4 => ####
      // // WARNING: These won't appear in VSCode's default TOC generator
      // // because it parses markdown *before* MPE parses it
      // // I've made snippets "h1" through "h6" that expands to <'#' * header num.> <tab stop 1>
      // // eg. h4 => #### <tab stop 1>
      // markdown = markdown.replace(/^[h#]([1-6]) (.+)$/gm, ($0,$1,$2) => '#'.repeat(parseInt($1)) + ` ${$2}`)

      // Book reference with exercise "path"
      markdown = markdown.replace(/^@([^:]+):([\d\-,]+)(\+?)#([\w\d/]+)$/gm, ($0, $book, $page, $pageplus, $exercise) => `*${$book}: p.${$page}${$pageplus ? '-' + (parseInt($page)+1) : ''}, ex.${$exercise}*`)
      // Simple book reference
      markdown = markdown.replace(/^@([^:]+):([\d\-,]+)(\+?)$/gm, ($0, $book, $page, $pageplus) => `*${$book}: p.${$page}${$pageplus ? '-' + (parseInt($page)+1) : ''}*`)

      // /* ----------------
      //       LaTeX
      // --------------- */

      markdown = markdown.replace(/\${1,2}([^$]+)\${1,2}/gm, (ret, $1) => {
      //   schoolsystKaTeX_escapes.forEach(e => {
      //     ret = ret.replace('\\'+e, encodeHtmlEntity(e))
      //   })
      //   ret = ret.replace(/#(\w+)\{((.+))\}/, ($0,color,content) => ` \\color{${colourNameToHex(color)}}{${content}} `)
      //   schoolsystKaTeX_escapes.forEach(e => {
      //     ret = ret.replace(encodeHtmlEntity(e), decodeHtmlEntity(e))
      //   })


        return ret
      })

      return resolve(markdown)
    })
  },
  onDidParseMarkdown: function (html) {
    return new Promise((resolve, reject) => {
      html = html.replace('<head>','<head><link rel="stylesheet" href="https://github.com/ewen-lbh/school-stuff/deps/fonts/fonts.css">')
      html = html.replace(/<a href="#fnref(\d+)" class="footnote-backref">↩︎<\/a>/g, ($0,$1)=>'<a href="#fnref'+$1+'" class="footnote-backref">⤴</a>')
      return resolve(html)
    })
  }
}
