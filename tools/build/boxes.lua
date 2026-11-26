-- Turns ::: mission / lab / hint ... divs into labelled boxes.
-- If MOVE_ANSWERS=1, sections with class .answers are removed from chapters and collected at the end.
local labels = {mission="MISSION", keyidea="KEY IDEA", misconception="MISCONCEPTION", example="WORKED EXAMPLE",
  lab="LAB", hint="HINT", max="MAX THE AGENT", bridge="THE BIG PICTURE"}
function Div(el)
  for cls,_ in pairs(labels) do
    if el.classes:includes(cls) then
      el.classes:insert("box")
      return el
    end
  end
end
local move = os.getenv("MOVE_ANSWERS") == "1"
function Pandoc(doc)
  if not move then return doc end
  local body, answers, inans = {}, {}, false
  for _,b in ipairs(doc.blocks) do
    if b.t == "Header" and b.level <= 2 then
      inans = (b.level == 2 and b.classes:includes("answers"))
    end
    if inans then
      if b.t == "Header" then b.level = 2 end
      table.insert(answers, b)
    else
      table.insert(body, b)
    end
  end
  table.insert(body, pandoc.Header(1, {pandoc.Str("Answers"), pandoc.Space(), pandoc.Str("and"), pandoc.Space(), pandoc.Str("Feedback")}, pandoc.Attr("answers-and-feedback",{"answers-part"})))
  table.insert(body, pandoc.Para({pandoc.Emph({pandoc.Str("Try every Lab and Quick Check before reading these. Each block links back to its chapter.")})}))
  for _,b in ipairs(answers) do table.insert(body, b) end
  doc.blocks = body
  return doc
end
