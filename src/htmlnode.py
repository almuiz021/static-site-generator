class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None ):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {} 

    def to_html(self):
        raise NotImplementedError("")
    
    def props_to_html(self):
        if self.props:
            attributes = ""
            for keys,value in self.props.items():
                attribute = f'{keys} = "{value}" '
                attributes += attribute
            return attributes
    
    def __repr__(self):
            return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"



    