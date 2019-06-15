module.exports = {
  onWillParseMarkdown: function (markdown) {
    return new Promise((resolve, reject) => {

      /* ----------------
            MARKDOWN
      --------------- */
    
      // Underlined text: __text__ => <u>text</u>
      markdown = markdown.replace(/__(.+)__/gm, ($0, $1) => '<u>' + $1 + '</u>')
      // Newline (might remove): \n => <br>
      markdown = markdown.replace(/\\n(\s)/gm, ($0, $1) => '<br>' + $1)

      // Dotted arrows
      markdown = markdown.replace('...>','···>')
      markdown = markdown.replace('..>','··>')

      // Special arrows
      markdown = markdown.replace('|_>', '↳')

      
      // Named headers: #4 => ####
      // WARNING: These won't appear in VSCode's default TOC generator
      // because it parses markdown *before* MPE parses it
      // I've made snippets "h1" through "h6" that expands to <'#' * header num.> <tab stop 1>
      // eg. h4 => #### <tab stop 1>
      markdown = markdown.replace(/^[h#]([1-6]) (.+)$/gm, ($0,$1,$2) => '#'.repeat(parseInt($1)) + ` ${$2}`)

      // Book reference with exercise "path"
      markdown = markdown.replace(/^@([^:]+):([\d\-,]+)(\+?)#([\w\d/]+)$/gm, ($0, $book, $page, $pageplus, $exercise) => `*${$book}: p.${$page}${$pageplus ? '-' + (parseInt($page)+1) : ''}, ex.${$exercise}*`)
      // Simple book reference
      markdown = markdown.replace(/^@([^:]+):([\d\-,]+)(\+?)$/gm, ($0, $book, $page, $pageplus) => `*${$book}: p.${$page}${$pageplus ? '-' + (parseInt($page)+1) : ''}*`)

      // Colors
      markdown = markdown.replace(/[#@](\w+)\{([^}]+)}/gm, ($0, $1, $2) => {
        color = $1
        if ($1.match(/[0-9A-Fa-f]{3,6}/)) {
          color = '#' + color
        }
        ret = []
        $2.split('\n').forEach(l=>{ret.push(`<span style="color:${color} !important;">${l}</span>`)})
        return ret.join('\n')
      })

      /* ----------------
            LaTeX
      --------------- */
      // Ceil command: \ceil{thing} => \lceil thing \rceil
      markdown = markdown.replace(/\\ceil\{([^}]+)\}/gm, ($0, $1) => '\\lceil' + $1 + '\\rceil')
      // Floor command: \floor{thing} => \lfloor thing \rfloor
      markdown = markdown.replace(/\\floor\{([^}]+)\}/gm, ($0, $1) => '\\lfloor' + $1 + '\\rfloor')
      // Aliases only replaced inside LaTeX areas
      markdown = markdown.replace(/\${1,2}!?([^$]+)\${1,2}/gm, (ret,$1) => {
        // |->           ····> \mapsto
        //ret = ret.replace('|->', '\\mapsto ')

        // Function conversion! 
        // - set funcMapStyle to true to use map-style functions: f:x↦y
        // - set to false to use parenthesis-style functions: f(x)=y
        funcMapStyle = true
        if (funcMapStyle) {
          // all functions to map-style ( f:x↦y )
          ret = ret.replace(/([^\s\d]+)\s*\(\s*(\S)\s*\)\s*&?=/gm, ($0, f, x) => `${f}:${x}\\mapsto `)
        } else {
          // all functions to parenthesis-style ( f(x)=y )
          ret = ret.replace(/([^\s\d]+)\s*:\s*(\S)\s*\\mapsto\s+/gm, ($0, f, x) => `${f}(${x})=`)
        }

        return ret
      })
      // Auto-add \\ & aligned environment in display math when inner lines count is > 1
      markdown = markdown.replace(/^\$\$\n([^\$]+)\n\$\$$/gm, ($0, $1) => {
        lines = $1.split('\n').filter(l => !l.match(/^\s*$/))
        if (lines.length == 1) return $0

        retlines = ['$$\n\\begin{aligned}']
        retlines = []
        lines.forEach(line => {
          if (line.match(/\\\\$/)) {
            line = line.replace(/^([^\\]+)\\\\$/, ($0,$1)=>$1)
          }
          if (!line.match(/&/) && line.match(/=|>|<|(?:>=)|(?:<=)/)) {
            line = line.replace(/=|>|<|(?:>=)|(?:<=)/, $0 => '&'+$0)
          }
          retlines.push(line+'\\\\')
        });
        retlines.push('\\end{aligned}\n$$')

        return retlines.join('\n')
      })
      // Removes ! from $$! (to prevent default equation behavior)
      markdown = markdown.replace(/^\${2}!$/gm, ($0) => '$$')

      markdown += `\n\n<br><br><br>
      $$
      \\aleph \\;\\lang \\text{E\\u{w}en } \\Gamma \\text{e B} \\mathring{\\imath}\\text{h}\\alpha\\text{n} \\rang\\; \\nabla
      $$`

      return resolve(markdown)
    })
  },
  onDidParseMarkdown: function (html) {
    return new Promise((resolve, reject) => {
      html = html.replace('<head>','<head><link rel="stylesheet" href="https://github.com/ewen-lbh/school-stuff/deps/fonts/fonts.css">')
      
      return resolve(html)
    })
  }
}