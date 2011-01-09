//
//  HowOldViewController.m
//  HowOld
//
//  Created by Swizec on 1/9/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "HowOldViewController.h"

@implementation HowOldViewController
@synthesize yearPicker;
@synthesize pickerData;
@synthesize currentYear;

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
  NSInteger row = [yearPicker selectedRowInComponent:0];
  NSString *selected = [pickerData objectAtIndex:row];
  NSString *title = [[NSString alloc] initWithFormat:
                     @"you selected %@!", selected];
  UIAlertView *alert = [[UIAlertView alloc] initWithTitle:title
                                                 message : @"Thank you for choosing."
                                                 delegate:nil
                                       cancelButtonTitle :@"You are Welcome"             
                                       otherButtonTitles :nil];
  [alert show];
  [alert release];
  [title release];
}

- (void)viewDidLoad {
  currentYear = [self getCurrentYear];
  
  NSLog(@"year %d", currentYear);
  
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
