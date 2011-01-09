//
//  HowOldViewController.h
//  HowOld
//
//  Created by Swizec on 1/9/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface HowOldViewController : UIViewController 
<UIPickerViewDataSource , UIPickerViewDelegate>
{
  IBOutlet UIPickerView *yearPicker;
  NSArray *pickerData;
}

@property(nonatomic , retain) UIPickerView *yearPicker;
@property(nonatomic , retain) NSArray *pickerData;
@property(nonatomic) int currentYear;

-(IBAction)buttonPressed;
-(int)getCurrentYear;

@end