//
//  HowOldViewController.h
//  HowOld
//
//  Created by Swizec on 1/9/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <iAd/iAD.h>

@interface HowOldViewController : UIViewController 
<UIPickerViewDataSource , UIPickerViewDelegate, UITextFieldDelegate, ADBannerViewDelegate>
{
  IBOutlet UIPickerView *yearPicker;
  IBOutlet UITextField *celebrity;
  IBOutlet UIProgressView *fetchProgress;
  IBOutlet ADBannerView *adView;
  BOOL bannerIsVisible;
  NSArray *pickerData;
}

@property(nonatomic , retain) UIPickerView *yearPicker;
@property(nonatomic , retain) UITextField *celebrity;
@property(nonatomic , retain) UIProgressView *fetchProgress;
@property(nonatomic , retain) NSArray *pickerData;
@property(nonatomic) int currentYear;
@property(nonatomic,assign) BOOL bannerIsVisible;

extern NSInteger UNPOSSIBLE_YEAR;

-(IBAction) textFieldDoneEditing : (id) sender;
-(IBAction) backgroundTap:(id) sender;

-(IBAction)buttonPressed;
-(int)getCurrentYear;

-(IBAction)fetchDataInBackground;
-(void)reportResult:(NSInteger)birthYear;
-(void)noFound;

@end