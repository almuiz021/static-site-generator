class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        attributes = ""
        for keys,value in self.props.items():
            attribute = f' {keys}="{value}"'
            attributes += attribute
        return attributes
    
    def __repr__(self):
            return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
     def __init__(self, tag, value, props = None):
         super().__init__(tag, value, None, props)

     def to_html(self):
        if not self.value:
            raise ValueError("MUST HAVE VALUE")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
     
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("MUST HAVE TAG")
        if not self.children:
            raise ValueError("MUST HAVE CHILDREN")
        
        childrenTag =""
        for item in self.children:
            childrenTag += item.to_html()

        return f"<{self.tag}{self.props_to_html()}>{childrenTag}</{self.tag}>"
        
