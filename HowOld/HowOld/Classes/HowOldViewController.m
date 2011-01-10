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
#import "MixpanelAPI.h"

// impossible for anyone to be older than 100M years
NSInteger UNPOSSIBLE_YEAR = -100000000;

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
  [mixpanel track:@"Searched" 
       properties:[NSDictionary dictionaryWithObjectsAndKeys:celebrity.text, @"celebrity",
                   [NSString stringWithFormat:@"%d", [self getSelectedYear]], @"selectedYear", nil]];
  
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
  
  NSInteger birthYear = [self getBirthYear:trs];
  NSInteger deathYear = [self getDeathYear:trs];
  
  NSLog(@"birth: %d, death: %d", birthYear, deathYear);
  
  if (birthYear <= UNPOSSIBLE_YEAR) {
    [self noFound];
  } else if (deathYear > UNPOSSIBLE_YEAR) {
    [self reportResult:birthYear deathYear:deathYear];
  } else {
    [self reportResult:birthYear];
  }
  
  [parser release];
}

- (NSInteger)getBirthYear:(NSArray *)nodes {
  return [self getYearInWikipedia:nodes type:@"date of birth"];
}

- (NSInteger)getDeathYear:(NSArray *)nodes {
  return [self getYearInWikipedia:nodes type:@"date of death"];
}

- (NSInteger)getYearInWikipedia:(NSArray *)nodes type:(NSString *)type{
  
  NSError *error = NULL;
  NSRegularExpression *regexTitle = [NSRegularExpression regularExpressionWithPattern:type
                                                                              options:NSRegularExpressionCaseInsensitive
                                                                                error:&error];
  NSRegularExpression *regexYear = [NSRegularExpression regularExpressionWithPattern:@"([0-9]+)[ ]*(<span|</td|BC)"
                                                                             options:NSRegularExpressionCaseInsensitive
                                                                               error:&error];
  NSRegularExpression *regexYear2 = [NSRegularExpression regularExpressionWithPattern:@"([0-9]+)-[\-0-9 ]*(<span|</td|BC)"
                                                                              options:NSRegularExpressionCaseInsensitive
                                                                                error:&error];
  
  NSUInteger numberOfMatches;
  NSString *s, *s2;
  
  for (HTMLNode * tr in nodes) {
    
    s = [[tr firstChild] rawContents];
    numberOfMatches = [regexTitle numberOfMatchesInString:s
                                                  options:0
                                                    range:NSMakeRange(0, [s length])];
    
    if (numberOfMatches > 0) {
      NSArray *children = [tr findChildTags:@"td"];
      
      s2 = [[children objectAtIndex:1] rawContents];
      NSLog(@"%@", s2);
      NSArray *matches = [regexYear2 matchesInString:s2 
                                             options:0 
                                               range:NSMakeRange(0, [s2 length])];
      
      if ([matches count] <= 0) {
        NSLog(@"not match!");
        matches = [regexYear matchesInString:s2 
                                     options:0 
                                       range:NSMakeRange(0, [s2 length])];
      }
      
      if ([matches count] > 0) {
        NSTextCheckingResult *match = [matches objectAtIndex:[matches count]-1];
        NSRange BCrange = [s2 rangeOfString:@"BC"];
        NSInteger year = [[s2 substringWithRange:[match rangeAtIndex:0]] intValue];
        if (BCrange.length > 0) {
          return -year;
        } else {
          return year;
        }
      }
    }
  }
  
  
  return UNPOSSIBLE_YEAR;
}


- (void)requestFailed:(ASIHTTPRequest *)request
{
  NSError *error = [request error];
  
  [self noFound];
}

-(NSInteger)getSelectedYear {
  NSInteger row = [yearPicker selectedRowInComponent:0];
  NSString *selected = [pickerData objectAtIndex:row];
  NSRange BCrange = [selected rangeOfString:@"BC"];
  NSInteger selectedYear;
  if (BCrange.length > 0) {
    selectedYear = -[[selected substringWithRange:NSMakeRange(0, 4)] intValue];
  } else {
    selectedYear = [selected intValue];
  }
  
  return selectedYear;
}

- (void)reportResult:(NSInteger)birthYear {
  NSInteger selectedYear = [self getSelectedYear];
  
  NSString *title;
  
  if (selectedYear >= 0) {
    title = [[NSString alloc] initWithFormat:
                       @"In %d", selectedYear];
  } else {
    title = [[NSString alloc] initWithFormat:
                       @"In %d BC", selectedYear];
  }

  NSString *message;
  
  if (birthYear > selectedYear) {
    message = [[NSString alloc] initWithFormat:@"%@ would take another %d years to be born!", celebrity.text, birthYear-selectedYear];
  } else {
    message = [[NSString alloc] initWithFormat:@"%@ was %d years old!", celebrity.text, selectedYear-birthYear];
  }
  
  [self showMessage:title message:message button:@"Wow thanks!"];
}

-(void)reportResult:(NSInteger)birthYear deathYear:(NSInteger)deathYear {
  NSInteger selectedYear = [self getSelectedYear];
  
  if (deathYear < selectedYear) {
    NSString *title;
    if (selectedYear >= 0) {
      title = [[NSString alloc] initWithFormat:
                         @"In %d", selectedYear];
    } else {
      title = [[NSString alloc] initWithFormat:
                         @"In %d BC", selectedYear];
    }
    
    NSString *message = [[NSString alloc] initWithFormat:@"%@ died at %d and was dead for %d years :(", 
                                              celebrity.text, deathYear-birthYear, selectedYear-deathYear, deathYear-birthYear];
    
    [self showMessage:title message:message button:@"Poor dude."];
  } else {
    [self reportResult:birthYear];
  }
}

-(void)showMessage:(NSString *)title message:(NSString *)message button:(NSString *)button {
  UIAlertView *alert = [[UIAlertView alloc] initWithTitle:title
                                                  message:message
                                                 delegate:nil
                                        cancelButtonTitle:button
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
  mixpanel = [MixpanelAPI sharedAPI];
	
  [mixpanel track:@"Application Open"];
  
  currentYear = [self getCurrentYear];
  
  NSMutableArray *array = [NSMutableArray arrayWithCapacity:currentYear];
  for (int i=currentYear; i>=0; i--) {
    [array addObject:[NSString stringWithFormat:@"%d", i]];
  }
  for (int i=1; i<=4000; i++) {
    [array addObject:[NSString stringWithFormat:@"%d BC", i]];
  }
  self.pickerData = array;
  
  adView = [[ADBannerView alloc] initWithFrame:CGRectZero];
  adView.frame = CGRectOffset(adView.frame, 0, -50);
  adView.requiredContentSizeIdentifiers = [NSSet setWithObject:ADBannerContentSizeIdentifierPortrait];
  adView.currentContentSizeIdentifier = ADBannerContentSizeIdentifierPortrait;
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
