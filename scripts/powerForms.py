from genLib import checkKey
from genLib import sortKey
def pureGen():
 return True
class formTemplate:
 props={}
 def __init__(self, name, genInfo):
  self.props={}
  self.name=name
  self.genInfo=genInfo
  self.genInfo(self)
 def genEntity(self,entity):
  outStr=''
  index=list(self.props)
  for item in index:
   mandatory=self.props.get(item)
   if checkKey(item,entity) or mandatory:
    outStr+='\\newline\\textbf{'
    outStr+=item
    outStr+=': }'
    outStr+=entity.get(item)
  return outStr

def genEntity(entity):
 outStr='\\paragraph{Форма Могущества} является первоначальным их описанием и заранее определяет многие свойства Могущества. Самые распространенные формы и их свойства:\\begin{itemize}'
 for form in getForms():
  outStr+=form.genInfo(form)
 outStr+='\\end{itemize}'
 return outStr

def getForms():
 forms=[]
 forms.append(formTemplate('Снаряд',genProjectileInfo))
 forms.append(formTemplate('Бомба',genBombInfo))
 forms.append(formTemplate('Метка',genMarkInfo))
 forms.append(formTemplate('Область',genRegionInfo))
 forms.append(formTemplate('Призыв',genSummonInfo))
 forms.append(formTemplate('Наговор',genHexInfo))
 return forms

def genProjectileInfo(self):
 outStr='\\item\\textbf{'+self.name+',} который герой отправляет в цель, нанося повреждения, как Дальнобойное оружие, за тем исключением, что вместо Стрельбы(ЛВ) при проверках Меткости герой использует Концентрацию(МХM)'
 prop='Дистанция'
 self.props[prop]=False
 outStr+='\\newline\\textbf{'+prop+'} Снаряда определяется, как Ближняя 20 / Дальняя 40, если не сказано иначе.'
 
 prop='Тип Повреждений'
 self.props[prop]=True
 outStr+='\\newline В описании Снаряда обязательно должны быть указаны \\textbf{'+prop

 prop='Бонус Повреждений'
 self.props[prop]=True
 outStr+='} и \\textbf{'+prop+'}.'

 prop='КУ'
 self.props[prop]=False
 outStr+='\\newline\\textbf{'+prop+'} Снаряда равен 20, если не сказано иначе.'

 prop='Скорострельность'
 self.props[prop]=False
 outStr+='\\newline\\textbf{'+prop+'} Снаряда рана 1, если не сказано иначе. Высокая Скорострельность позволяет согласно правилам поразить несколько целей или нанести больший урон по одной цели за одну активацию способности.'
 return outStr

def genBombInfo(self):
 outStr='\\item\\textbf{'+self.name+'} которую герой метает во врагов. Для того, чтобы хорошо бросить Бомбу, герою все еще нужно совершить проверку Меткости по обычным правилам бросания Гранат, но МХМ и Концентрация определяют, насколько мощной получится Бомба. Так же пока Бомба не брошена, ее \\textbf{Стоимость Поддержания} равна нулю.'

 prop='Радиус Взрыва'
 self.props[prop]=False
 outStr+='\\newline\\textbf{'+prop+'} Бомбы равен \\textbf{МХМ+1(мин 2)}, если не сказано иначе.'

 prop='Сила Взрыва'
 self.props[prop]=False
 outStr+='\\newline\\textbf{'+prop+'} Бомбы равна \\textbf{10+Концентрация(МХМ)}, если не сказано иначе.'

 outStr+='\\newline В описании Бомбы обязательно должны быть описаны эффекты взрыва.'
 return outStr

def genMarkInfo(self):
 outStr='\\item\\textbf{'+self.name+',} котрорую герой накладывает на предмет или существо. Если существо не хочет, чтобы метка была наложена, герою надо совершить проверку Дб(Рукопашный бой) против Зщ цели, чтобы активировать Метку. В случае неудачи проверки, Метка остается в руке героя и он может попытаться совершить атаку в следующий ход, чтобы наложить метку, однако в этом случае герою могут легко помешать, Прервав активацию. Герой может Прервать активацию Метки по собственному желанию. Пока Метка находится в руке героя, рука считается занятой и ей он не может активировать другие Могущества. Так же пока Метка не наложена на цель, ее \\textbf{Стоимость Поддержания} равна нулю.'
 prop='Сопротивление'
 self.props[prop]=False
 outStr+='В описании Метки обязательно должно быть указано \\textbf{'+prop+'} цели.'
 return outStr

def genRegionInfo(self):
 outStr='\\item\\textbf{'+self.name+'[Уточнение]} вокруг героя, которая накладывает на всех существ, которые в нее попали определенные эффекты, исключая самого героя.'

 outStr+='\\newline Если не указано \\textbf{Уточнение}, Область является Кругом вокруг героя.'
 outStr+='\\newline \\textbf{Формы Области}:'
 outStr+='\\begin{itemize}'
 outStr+='\\item[--] \\textbf{Круг} вокруг героя. \\textbf{Дистанция} определяет радиус круга.'
 outStr+='\\item[--] \\textbf{Периметр} очерченный героем. Это должна быть замкнутая линия без самопересечений. \\textbf{Дистанция} определяет 2 максимально удаленные друг от друга точки периметра.'
 outStr+='\\item[--] \\textbf{Конус} \\tbd'
 outStr+='\\item[--] \\tbd'
 outStr+='\\end{itemize}'

 prop='Дистанция'
 self.props[prop]=True
 outStr+='\\textbf{'+prop+'} Области определяет максимальное удаление от героя, на котором накладываются эффекты области во время ее активации.'

 prop='Сопротивление'
 self.props[prop]=True
 outStr+='\\newline В описании Области обязательно должно быть указано \\textbf{'+prop+'} существ. Используйте Коллективной проверки, чтобы быстрее определить влияние Области на группу существ.'
 return outStr

def genSummonInfo(self):
 outStr='\\item\\textbf{'+self.name+'} позволяет переместить из иных измерений существа и предметы, не принадлежащие этому миру. Призванные существа исполняют все приказы призывателя. По истечении времени Призыва они \\textit{обычно} возвращаются в родное измерение, но могут и задержаться. В этом случае контроль призывателя над их действиями прекращается и обычно существа остаются очень разозлены фактом призыва и хотят отомстить.'

 prop='Дистанция'
 self.props[prop]=False
 outStr+='\\newline Если не указана \\textbf{'+prop+'} Призыва, то призванный предмет оказывается в руке призывателя, а существо - в свободной соседней с призывателем клетке. Призванное существо не может по своей воле отойти от призывателя дальше, чем указано в Дистанции. Если призванные существо или предмет случайно или благодаря усилиям других существ удаляться дальше, чем указано в Дистанции, Призыв немедленно Прерывается.'

 prop='Сопротивление'
 self.props[prop]=True
 outStr+='\\newline В описании Призыва обязательно должно быть указано \\textbf{'+prop+'} призыва. Призываемые существа используют свою Волю, чтобы сопротивляться призыву, а предметы имеют статичное значение Сопротивления.'
 return outStr

def genHexInfo(self):
 outStr='\\item\\textbf{'+self.name+'} является дистанционным Могуществом, которая сразу накладывается на цель. Если герой не видит цель, но она находится в пределах \\textbf{Дистанции} Наговора, ему надо совершить проверку Наведения. В случае провала проверки, активация считается Прерванной. Если цель находится или покидает пределы Дистанции Наговора, активация автоматически Прерывается.'

 prop='Дистанция'
 self.props[prop]=True
 outStr+='\\newline В описании Наговора обязательно должна быть указана \\textbf{'+prop+'}'

 prop='Сопротивление'
 self.props[prop]=True
 outStr+='\\newline В описании Наговора обязательно должно быть указано \\textbf{'+prop+'} цели'
 return outStr
