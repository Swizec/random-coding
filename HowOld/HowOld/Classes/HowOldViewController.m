//
//  HowOldViewController.m
//  HowOld
//
//  Created by Swizec on 1/9/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "HowOldViewController.h"
#import "ASIHTTPRequest.h"
#import "HTMLParser.h"
#import "HTMLNode.h"

@implementation HowOldViewController
@synthesize yearPicker;
@synthesize pickerData;
@synthesize currentYear;
@synthesize celebrity;
@synthesize fetchProgress;
@synthesize bannerIsVisible;

- (void)didReceiveMemoryWarning {
	// Releases the view if it doesn't have a superview.
    [super didReceiveMemoryWarning];
	
	// Release any cached data, images, etc that aren't in use.
}

- (void)viewDidUnload {
	// Release any retained subviews of the main view.
	// e.g. self.myOutlet = nil;
}


- (void)dealloc {
  [adView release];
  [yearPicker release];
  [celebrity release];
  [pickerData release];
  [super dealloc];
}

-(IBAction)buttonPressed
{
  [self fetchDataInBackground];  
}

- (IBAction)fetchDataInBackground
{
  
  NSString *encodedCelebrity = (NSString *)CFURLCreateStringByAddingPercentEscapes(
                                                                                   NULL,
                                                                                   (CFStringRef)celebrity.text,
                                                                                   NULL,
                                                                                   (CFStringRef)@"!*'();:@&=+$,/?%#[]",
                                                                                   kCFStringEncodingUTF8 );
  NSString *_url = [NSString stringWithFormat:@"http://en.wikipedia.org/w/index.php?search=%@", encodedCelebrity];
  NSURL *url = [NSURL URLWithString:_url];
  
  ASIHTTPRequest *request = [ASIHTTPRequest requestWithURL:url];
  fetchProgress.progress = 0.0;
  [request setDownloadProgressDelegate:fetchProgress]; 
  [request setDelegate:self];
  [request startAsynchronous];
}

- (void)requestFinished:(ASIHTTPRequest *)request
{
  // Use when fetching text data
  NSString *responseString = [request responseString];
  
  NSError *error = NULL;
  HTMLParser *parser = [[HTMLParser alloc] initWithString:responseString 
                                                    error:error];
  
  if (error) {
    NSLog(@"error: %@", error);
    return;
  }
  
  HTMLNode *body = [parser body];
  
  
  HTMLNode *persondata = [body findChildWithAttribute:@"class" matchingName:@"persondata" allowPartial:NO];
  
  NSArray * trs = [persondata findChildTags:@"tr"];
  
  NSRegularExpression *regexTitle = [NSRegularExpression regularExpressionWithPattern:@"date of birth"
                                                                              options:NSRegularExpressionCaseInsensitive
                                                                                error:&error];
  NSRegularExpression *regexYear = [NSRegularExpression regularExpressionWithPattern:@"([0-9]+)(<span|</td)"
                                                                             options:NSRegularExpressionCaseInsensitive
                                                                               error:&error];
  NSUInteger numberOfMatches;
  NSString *s, *s2;
  BOOL foundIt = NO;
  
  for (HTMLNode * tr in trs) {
    
    s = [[tr firstChild] rawContents];
    numberOfMatches = [regexTitle numberOfMatchesInString:s
                                                  options:0
                                                    range:NSMakeRange(0, [s length])];
    if (numberOfMatches > 0) {
      foundIt = YES;
      s2 = [[[tr findChildTags:@"td"] objectAtIndex:1] rawContents];
      NSDateFormatter *dateFormat = [[NSDateFormatter alloc] init];
      NSArray *matches = [regexYear matchesInString:s2 
                                           options:0 
                                             range:NSMakeRange(0, [s2 length])];
      
      NSTextCheckingResult *match = [matches objectAtIndex:[matches count]-1];
      [self reportResult:[[s2 substringWithRange:[match rangeAtIndex:0]] intValue]];
    }
  }
  
  if (!foundIt) {
    [self noFound];
  }
  
  [parser release];
  /*[regexTitle release];
  [regexYear release];
  [trs release];
  [body release];*/
}

- (void)requestFailed:(ASIHTTPRequest *)request
{
  NSError *error = [request error];
  
  [self noFound];
}

- (void)reportResult:(NSInteger)birthYear {
  NSLog(@"birth: %d", birthYear);
  
  NSInteger row = [yearPicker selectedRowInComponent:0];
  NSString *selected = [pickerData objectAtIndex:row];
  NSInteger selectedYear = [selected intValue];
  
  NSString *title = [[NSString alloc] initWithFormat:
                     @"In %d", selectedYear];
  NSString *message = [[NSString alloc] initWithFormat:@"%@ was %d years old!", celebrity.text, selectedYear-birthYear];
  
  UIAlertView *alert = [[UIAlertView alloc] initWithTitle:title
                                                    message:message
                                                   delegate:nil
                                          cancelButtonTitle:@"Wow thanks!"
                                          otherButtonTitles:nil];
  
  [alert show];
  
  [alert release];
}

-(void)noFound {
  UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"Oh dear!"
                                                  message:@"Couldn't find anything on wikipedia"
                                                 delegate:nil
                                        cancelButtonTitle:@":("
                                        otherButtonTitles:nil];
  
  [alert show];
  
  [alert release];
}

-(IBAction) textFieldDoneEditing : (id) sender{
  [sender resignFirstResponder];
}

-(IBAction) backgroundTap:(id) sender{
  [self.celebrity resignFirstResponder];
}

- (void)viewDidLoad {
  currentYear = [self getCurrentYear];
  
  NSMutableArray *array = [NSMutableArray arrayWithCapacity:currentYear];
  for (int i=currentYear; i>=0; i--) {
    [array addObject:[NSString stringWithFormat:@"%d", i]];
  }
  self.pickerData = array;
  
  adView = [[ADBannerView alloc] initWithFrame:CGRectZero];
  adView.frame = CGRectOffset(adView.frame, 0, -50);
  adView.requiredContentSizeIdentifiers = [NSSet setWithObject:ADBannerContentSizeIdentifier320x50];
  adView.currentContentSizeIdentifier = ADBannerContentSizeIdentifier320x50;
  [self.view addSubview:adView];
  adView.delegate=self;
  self.bannerIsVisible=NO;
  
  [super viewDidLoad];
}

#pragma mark Picker data source methods
-(NSInteger)numberOfComponentsInPickerView:(UIPickerView *)pickerView
{
  return 1;
}

-(NSInteger)pickerView:(UIPickerView *)pickerView
numberOfRowsInComponent:(NSInteger)component
{
  return [pickerData count];
}

#pragma mark Picker delegate method
-(NSString *)pickerView:(UIPickerView *)pickerView
            titleForRow:(NSInteger)row
           forComponent:(NSInteger)component 
{
  return[pickerData objectAtIndex:row];
}

-(int)getCurrentYear {
  NSDate *today = [[[NSDate alloc] init] autorelease];
  NSDateFormatter *dateFormat = [[[NSDateFormatter alloc] init] autorelease];
  [dateFormat setDateFormat:@"yyyy"];
  
  return [[dateFormat stringFromDate:today] intValue];
}

- (void)bannerViewDidLoadAd:(ADBannerView *)banner
{
  if (!self.bannerIsVisible)
  {
    [UIView beginAnimations:@"animateAdBannerOn" context:NULL];
    // banner is invisible now and moved out of the screen on 50 px
    banner.frame = CGRectOffset(banner.frame, 0, 50);
    [UIView commitAnimations];
    self.bannerIsVisible = YES;
  }
}

- (void)bannerView:(ADBannerView *)banner didFailToReceiveAdWithError:(NSError *)error
{
  if (self.bannerIsVisible)
  {
    [UIView beginAnimations:@"animateAdBannerOff" context:NULL];
    // banner is visible and we move it out of the screen, due to connection issue
    banner.frame = CGRectOffset(banner.frame, 0, -50);
    [UIView commitAnimations];
    self.bannerIsVisible = NO;
  }
}

@end
