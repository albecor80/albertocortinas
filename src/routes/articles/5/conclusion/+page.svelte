<script>
    import IconBar from "$lib/visuals/IconBar.svelte";    
    import { onMount } from "svelte";
  
    export let totalBilling = 4636543; 
    let currentBilling = 0; 
    let formattedBilling = "0 €"; 

    let billingOptions = [
        { label: "Total", value: totalBilling, percentage: 37.5 },
        { label: "City", value: 3459980, percentage: 42.2 },
        { label: "Resort", value: 1176563, percentage: 28.0 }
    ];


    export let totalCancellations = 44010;
    let currentCancellations = 0; 

    let cancellationOptions = [
        { label: "Total", value: totalCancellations },
        { label: "City", value: 32972 },
        { label: "Resort", value: 11038 }
    ];

    let selectedBilling = billingOptions[0]; // Default to totalBilling
    let selectedCancellations = cancellationOptions[0]; // Default to totalCancellations


    let percentage = parseFloat(selectedBilling.percentage); // Reactive percentage

    function updateValues(option) {
        selectedBilling = billingOptions.find(opt => opt.label === option.label);
        selectedCancellations = cancellationOptions.find(opt => opt.label === option.label);

        // Animate counters
        animateCounter(selectedBilling.value, "billing");
        animateCounter(selectedCancellations.value, "cancellations");

        // Update percentage
        percentage = parseFloat(selectedBilling.percentage);
    }
    onMount(() => {
        animateCounter(selectedBilling.value, "billing");
        animateCounter(selectedCancellations.value, "cancellations");
    });

    function animateCounter(targetValue, type) {
        const duration = 500; 
        const start = performance.now();
        let initialValue = type === "billing" ? currentBilling : currentCancellations;

        function animate(now) {
            const elapsed = now - start;
            const progress = Math.min(elapsed / duration, 1); 
            if (type === "billing") {
                currentBilling = Math.round(initialValue + progress * (targetValue - initialValue)); 
                formattedBilling = new Intl.NumberFormat("es-ES", {
                    style: "currency",
                    currency: "EUR",
                    minimumFractionDigits: 0, 
                    maximumFractionDigits: 0, 
                }).format(currentBilling); 
            } else if (type === "cancellations") {
                currentCancellations = Math.round(initialValue + progress * (targetValue - initialValue));
            }

            if (progress < 1) {
                requestAnimationFrame(animate);
            }
        }

        requestAnimationFrame(animate);
    }

</script>

<div class="flex  min-h-screen">
    <div class="flex flex-col w-1/2">
        <div class="flex flex-col p-24 items-center justify-center my-auto">

            <p class="text-gray-600 p-8   text-xl mt-0">focus on <span class="font-bold">hotels based in cities</span> rather than resorts, they accumulate the majority of cancellations</p>
            <p class="text-gray-600 p-8   text-xl mt-0">consider that the cancellations rise in the <span class="font-bold">summer months </span>, anticipate and offer alternatives to customers</p>
            <p class="text-gray-600 p-8   text-xl mt-0">create flexible alternatives for  <span class="font-bold">local (portuguese) customers</span> and <span class="font-bold">mid cost fares </span> travels around 65 € as they are the most suitable to cancel reservations </p>

            
        </div>
    </div>
    <div class="flex bg-[#96DBC9] flex-col w-1/2">
        <h1 class="my-auto p-8">Ready to take control on hotel reservation cancellations?</h1>

    </div>
</div>
