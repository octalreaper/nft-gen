from PIL import ImageColor, Image, ImageDraw

c = ImageColor.colormap
n = len( c )

cols        = 4
rows        = ((n-1) // cols) +1
cellHeight  = 30
cellWidth   = 170
imgHeight   = cellHeight * rows
imgWidth    = cellWidth * cols

i = Image.new( "RGB", (imgWidth,imgHeight), (0,0,0) )
a = ImageDraw.Draw( i )

for idx, name in enumerate( c ):
    y0 = cellHeight * (idx // cols)
    y1 = y0 + cellHeight
    x0 = cellWidth * (idx % cols)
    x1 = x0 + (cellWidth / 4)

    a.rectangle( [ x0, y0, x1, y1 ], fill=name, outline='black' )
    a.text( ( x1+1, y0+10 ), name, fill='white' )

i.save( 'color_chart.png' )
