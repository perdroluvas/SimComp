import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { useForm } from "react-hook-form";
import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormDescription,
  FormMessage,
} from "@/components/ui/form";

export default function Result() {
  const navigate = useNavigate();
  const form = useForm({
    defaultValues: {
      result: "Simulation completed successfully!",
    },
  });

  return (
    <div className="container mx-auto p-8">
      <h1 className="text-3xl font-bold mb-4">Simulation Results</h1>
      <Form {...form}>
        <form className="space-y-4">
          <FormField
            name="result"
            control={form.control}
            render={({ field }) => (
              <FormItem>
                <FormLabel>Results</FormLabel>
                <FormControl>
                  <textarea 
                    className="min-h-[100px] w-full p-2 border rounded-md" 
                    readOnly 
                    {...field} 
                  />
                </FormControl>
                <FormDescription>Simulation results will be displayed here.</FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <div className="flex gap-4">
            <Button variant="outline" onClick={() => navigate("/simulation")}>
              Back to Simulation
            </Button>
          </div>
        </form>
      </Form>
    </div>
  );
}
