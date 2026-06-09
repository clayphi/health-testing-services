-- Put the entire S6 Feature Comparison Matrix on landscape pages.
-- S6's tables are 14 columns of prose (lab networks, UX notes) that get
-- crushed/clipped in portrait. S5's coverage matrix is also wide but its cells
-- are short (YES/NO/CALC) and fit fine in portrait, so it is left alone.
-- Wrapping the whole S6 section (heading + all sub-tables) in ONE landscape div
-- lets the sub-tables flow across consecutive landscape pages without a forced
-- page break (and white space) before each individual table.
function Pandoc(doc)
  local blocks = doc.blocks
  local out = {}
  local i = 1
  while i <= #blocks do
    local b = blocks[i]
    if b.t == "Header" and b.level == 2
       and pandoc.utils.stringify(b):match("^S6%.") then
      local section = { b }
      i = i + 1
      while i <= #blocks and not (blocks[i].t == "Header" and blocks[i].level == 2) do
        section[#section + 1] = blocks[i]
        i = i + 1
      end
      out[#out + 1] = pandoc.Div(section, pandoc.Attr("", { "landscape" }))
    else
      out[#out + 1] = b
      i = i + 1
    end
  end
  return pandoc.Pandoc(out, doc.meta)
end
