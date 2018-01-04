# ================================= IMPORT ================================= #
# STATUS: ENABLE TO UPDATE/EDIT
import sys
sys.path.insert(0, './engine')
import engine

# >> ADD HIVE LIST HERE
hives = [
    './hives/queen',
    './hives/body',
    './hives/link',
    './hives/div',
    './hives/navigation',
    './hives/container',
    './hives/footer',
    './hives/card',
    './hives/paper',
    './hives/fabric',
    './hives/form',
    './hives/button',
    './hives/planet',
    './hives/heading',
    './hives/line',
    './hives/tweak',
]

engine.pull(hives)

# >> ADD IMPORT HIVE HERE
import body
import link
import div
import navigation
import container
import footer
import card
import paper
import fabric
import form
import button
import planet
import heading
import line
import tweak

# =============================== COMPONENTS =============================== #
# STATUS: ENABLE TO UPDATE/EDIT
# >> ADD NEW COMPONENTS HERE
components = [
    body.Body().draw(),
    link.Link().draw(),
    div.Div().draw(),
    navigation.Navigation().draw(),
    container.Container().draw(),
    footer.Footer().draw(),
    card.Card().draw(),
    paper.Paper().draw(),
    fabric.Fabric().draw(),
    form.Form().draw(),
    button.Button().draw(),
    planet.Planet().draw(),
    heading.Heading().draw(),
    line.Line().draw(),
    tweak.Tweak().draw(),
]

# ================================ POINTERS ================================ #
# STATUS: DONT CHANGE ANYTHING
pointers = ''

# ================================= UNPACK ================================= #
# STATUS: DONT CHANGE ANYTHING
for component in components:
	for unpack in component:
		pointers += unpack.replace('}', '} ')

# ================================= UPDATE ================================= #
# STATUS: DONT CHANGE ANYTHING
engine.update(pointers)