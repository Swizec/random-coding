//
//  HowOldViewController.m
//  HowOld
//
//  Created by Swizec on 1/9/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "HowOldViewController.h"
#import "ASIHTTPRequest.h"

@implementation HowOldViewController
@synthesize yearPicker;
@synthesize pickerData;
@synthesize currentYear;
@synthesize celebrity;
@synthesize fetchProgress;

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
    [super dealloc];
}

-(IBAction)buttonPressed
{
  [self grabURLInBackground];  

  /*
  ASIHTTPRequest *request = [ASIHTTPRequest requestWithURL:url];
  [request startSynchronous];
  NSError *error = [request error];
  if (!error) {
    NSString *response = [request responseString];
    
    NSLog(response);
  } else {
    NSLog([error localizedDescription]);
  }*/
  
  NSInteger row = [yearPicker selectedRowInComponent:0];
  NSString *selected = [pickerData objectAtIndex:row];
  NSString *title = [[NSString alloc] initWithFormat:
                     @"you selected %@!", selected];
  UIAlertView *alert = [[UIAlertView alloc] initWithTitle:title
                                                 message : @"Thank you for choosing."
                                                 delegate:nil
                                       cancelButtonTitle :celebrity.text
                                       otherButtonTitles :nil];
  [alert show];
  [alert release];
  [title release];
}

- (IBAction)grabURLInBackground
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
  
  //NSLog(@"%@", responseString);
}

- (void)requestFailed:(ASIHTTPRequest *)request
{
  NSError *error = [request error];
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
  //[array release];
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

@end
