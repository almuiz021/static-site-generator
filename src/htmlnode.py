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
                attribute = f' {keys} = "{value}"'
                attributes += attribute
            return attributes
    
    def __repr__(self):
            return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
     def __init__(  self,tag, value, props = None):
         super().__init__(tag, value,None,props)

     def to_html(self):
        if not self.value:
            raise ValueError("MUST HAVE VALUE")
        if self.tag is None:
            return self.value
        attributes = self.props_to_html()    
        if attributes is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{attributes}>{self.value}</{self.tag}>"




    