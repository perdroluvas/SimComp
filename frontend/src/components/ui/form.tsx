// Import React and necessary hooks
import * as React from "react"
// Import Radix UI's Label primitive
import * as LabelPrimitive from "@radix-ui/react-label"
// Import Slot for component composition
import { Slot } from "@radix-ui/react-slot"
// Import React Hook Form utilities
import {
  Controller,         // For controlled components
  type ControllerProps,    // Type for Controller props
  type FieldPath,          // Type for field path
  type FieldValues,        // Type for field values
  FormProvider,       // Context provider for the form
  useFormContext,     // Hook to access form context
  useFormState,       // Hook to access form state
} from "react-hook-form"

// Import utility for className concatenation
import { cn } from "@/lib/utils"
// Import your custom Label component
import { Label } from "@/components/ui/label"

// Alias FormProvider as Form for easier usage
const Form = FormProvider

// Type for the context value of a form field
type FormFieldContextValue<
  TFieldValues extends FieldValues = FieldValues,
  TName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>,
> = {
  name: TName // The name of the field
}

// Create a context for form fields
const FormFieldContext = React.createContext<FormFieldContextValue>(
  {} as FormFieldContextValue // Default value (empty object, casted)
)

// FormField component wraps Controller and provides field name context
const FormField = <
  TFieldValues extends FieldValues = FieldValues,
  TName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>,
>({
  ...props
}: ControllerProps<TFieldValues, TName>) => {
  return (
    // Provide the field name to children via context
    <FormFieldContext.Provider value={{ name: props.name }}>
      <Controller {...props} />
    </FormFieldContext.Provider>
  )
}

// Custom hook to access field context and state
const useFormField = () => {
  // Get field context (name)
  const fieldContext = React.useContext(FormFieldContext)
  // Get item context (id)
  const itemContext = React.useContext(FormItemContext)
  // Get form methods
  const { getFieldState } = useFormContext()
  // Get form state for this field
  const formState = useFormState({ name: fieldContext.name })
  // Get field state (error, etc.)
  const fieldState = getFieldState(fieldContext.name, formState)

  // Throw error if not used inside FormField
  if (!fieldContext) {
    throw new Error("useFormField should be used within <FormField>")
  }

  // Get id from item context
  const { id } = itemContext

  // Return useful values for field components
  return {
    id,
    name: fieldContext.name,
    formItemId: `${id}-form-item`, // For input id
    formDescriptionId: `${id}-form-item-description`, // For description id
    formMessageId: `${id}-form-item-message`, // For error message id
    ...fieldState, // Include error, etc.
  }
}

// Type for the context value of a form item
type FormItemContextValue = {
  id: string // Unique id for the item
}

// Create a context for form items
const FormItemContext = React.createContext<FormItemContextValue>(
  {} as FormItemContextValue // Default value (empty object, casted)
)

// FormItem component provides a unique id context for accessibility
function FormItem({ className, ...props }: React.ComponentProps<"div">) {
  // Generate a unique id for this item
  const id = React.useId()

  return (
    // Provide the id to children via context
    <FormItemContext.Provider value={{ id }}>
      <div
        data-slot="form-item"
        className={cn("grid gap-2", className)} // Add default and custom classes
        {...props}
      />
    </FormItemContext.Provider>
  )
}

// FormLabel component renders a label for the field
function FormLabel({
  className,
  ...props
}: React.ComponentProps<typeof LabelPrimitive.Root>) {
  // Get error state and form item id from context
  const { error, formItemId } = useFormField()

  return (
    <Label
      data-slot="form-label"
      data-error={!!error} // Add data attribute if error exists
      className={cn("data-[error=true]:text-destructive", className)} // Style if error
      htmlFor={formItemId} // Link label to input
      {...props}
    />
  )
}

// FormControl component renders the input/control for the field
function FormControl({ ...props }: React.ComponentProps<typeof Slot>) {
  // Get error state and ids from context
  const { error, formItemId, formDescriptionId, formMessageId } = useFormField()

  return (
    <Slot
      data-slot="form-control"
      id={formItemId} // Set input id
      aria-describedby={
        !error
          ? `${formDescriptionId}` // Describe with description if no error
          : `${formDescriptionId} ${formMessageId}` // Describe with both if error
      }
      aria-invalid={!!error} // Mark as invalid if error
      {...props}
    />
  )
}

// FormDescription component renders a description for the field
function FormDescription({ className, ...props }: React.ComponentProps<"p">) {
  // Get description id from context
  const { formDescriptionId } = useFormField()

  return (
    <p
      data-slot="form-description"
      id={formDescriptionId} // Set id for aria-describedby
      className={cn("text-muted-foreground text-sm", className)} // Style
      {...props}
    />
  )
}

// FormMessage component renders the error message for the field
function FormMessage({ className, ...props }: React.ComponentProps<"p">) {
  // Get error state and message id from context
  const { error, formMessageId } = useFormField()
  // If error, use its message; otherwise, use children
  const body = error ? String(error?.message) : props.children

  // If no message, render nothing
  if (!body) {
    return null
  }

  return (
    <p
      data-slot="form-message"
      id={formMessageId} // Set id for aria-describedby
      className={cn("text-destructive text-sm font-medium", className)} // Style
      {...props}
    >
      {body}
    </p>
  )
}

// Export all components and hooks for use in your forms
export {
  useFormField,
  Form,
  FormItem,
  FormLabel,
  FormControl,
  FormDescription,
  FormMessage,
  FormField,
}
