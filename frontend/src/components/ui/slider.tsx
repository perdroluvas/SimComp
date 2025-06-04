// components/ui/slider.tsx

import * as React from "react"
import * as RadixSlider from "@radix-ui/react-slider"
import { cn } from "@/lib/utils"

export interface SliderProps
  extends React.ComponentPropsWithoutRef<typeof RadixSlider.Root> {}

const Slider = React.forwardRef<
  React.ElementRef<typeof RadixSlider.Root>,
  SliderProps
>(({ className, ...props }, ref) => (
  <RadixSlider.Root
    ref={ref}
    className={cn(
      "relative flex w-full touch-none select-none items-center",
      className
    )}
    {...props}
  >
    <RadixSlider.Track className="relative h-2 w-full grow overflow-hidden rounded-full bg-secondary">
      <RadixSlider.Range className="absolute h-full bg-primary" />
    </RadixSlider.Track>
    {Array.isArray(props.value)
      ? props.value.map((_, i) => (
          <RadixSlider.Thumb
            key={i}
            className="block h-5 w-5 rounded-full border-2 border-primary bg-background shadow transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50"
          />
        ))
      : (
          <RadixSlider.Thumb
            className="block h-5 w-5 rounded-full border-2 border-primary bg-background shadow transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50"
          />
        )}
  </RadixSlider.Root>
))
Slider.displayName = "Slider"

export { Slider }
