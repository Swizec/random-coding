//
//  HTMLNode.h
//  StackOverflow
//
//  Created by Ben Reeves on 09/03/2010.
//  Copyright 2010 Ben Reeves. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <libxml/HTMLparser.h>
#import "HTMLParser.h"

@class HTMLParser;

#define ParsingDepthUnlimited 0
#define ParsingDepthSame -1
#define ParsingDepth size_t

typedef enum
{
	HTMLHrefNode,
	HTMLTextNode,
	HTMLUnkownNode,
	HTMLCodeNode,
	HTMLSpanNode,
	HTMLPNode,
	HTMLLiNode,
	HTMLUlNode,
	HTMLImageNode,
	HTMLOlNode,
	HTMLStrongNode,
	HTMLPreNode,
	HTMLBlockQuoteNode,
} HTMLNodeType;

@interface HTMLNode : NSObject 
{
	@public
	
	xmlNode * _node;
}

//Init with a lib xml node
-(id)initWithXMLNode:(xmlNode*)xmlNode;

-(NSArray*)findChildrenOfClass:(NSString*)className;
-(HTMLNode*)findChildOfClass:(NSString*)className;

-(NSArray*)findChildrenWithAttribute:(NSString*)attribute matchingName:(NSString*)className allowPartial:(BOOL)partial;
-(HTMLNode*)findChildWithAttribute:(NSString*)attribute matchingName:(NSString*)className allowPartial:(BOOL)partial;

//Gets the attribute value matching tha name
-(NSString*)getAttributeNamed:(NSString*)name;
NSString * getAttributeNamed(xmlNode * node, const char * nameStr);
void setAttributeNamed(xmlNode * node, const char * nameStr, const char * value);

//Find childer with the specified tag name
-(NSArray*)findChildTags:(NSString*)tagName;

//Looks for a tag name e.g. "h3"
-(HTMLNode*)findChildTag:(NSString*)tagName;

//Returns the first child element
-(HTMLNode*)firstChild;

//Contents of this node and children
-(NSString*)allContents;
NSString * allNodeContents(xmlNode*node);

//Returns the contents
-(NSString*)contents;

//Returns the class name
-(NSString*)className;

//Returns the tag name
-(NSString*)tagName;

//Returns the parent
-(HTMLNode*)parent;

//Returns the contents including html tags
-(NSString*)rawContents;
NSString * rawContentsOfNode(xmlNode * node);

//Returns the first level of children
-(NSArray*)children;

//Returns the node type if know
-(HTMLNodeType)nodetype;
HTMLNodeType nodeType(xmlNode* node);

@end
