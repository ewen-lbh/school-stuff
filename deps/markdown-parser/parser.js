module.exports = {
  onWillParseMarkdown: function(markdown) {
    return new Promise((resolve, reject)=> {
      markdown = markdown.replace(
        /`(.+)`/gm,
        ($0,$1)=>`<code>${$1}</code>`
    )
      markdown = markdown.replace(
        /\${2}/gm,
        '&displaymath;&displaymath;'
      )
      markdown = markdown.replace(
        /\$/gm,
        '\\`'
      )
      markdown = markdown.replace(
        /(?:&displaymath;){2}([\s\S]+)(?:&displaymath;){2}/gm,
        (_,$1)=>`<p style="text-align:center;">\`${$1}\`</p>`)
      markdown = markdown.replace(
        /note"(.+)"\{(.+)\}/gm,
        (_,note,cont)=>`underbrace(${cont})_("${note}")`
      )
      markdown += '\n<br><br><br>'
      return resolve(markdown)
    })
  },
  onDidParseMarkdown: function(html) {
    return new Promise((resolve, reject)=> {
      //html = `<script src="file:///D:/%23/Coding/projects/schoolsyst/asciimath.js"></script>${html}`
      html = `<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/latest.js?config=TeX-MML-AM_CHTML"></script>${html}`
      html = html.replace('<body', '<body onload="document.body.scrollTop = document.body.scrollHeight;"')
      return resolve(html)
    })
  }
}